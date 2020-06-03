from tablestore import *
from django.conf import settings
from django.utils import timezone as datetime
class OTS(object):
    """表格存储工具类"""
    @property
    def client(self):
        return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    def check_user_focus(self,author_id,follow_id):
        """判断用户是否已经关注了文章作者"""
        table_name = "user_relation_table"

        # 2. 主键列
        primary_key = [
            ('user_id', author_id), # 作者
            ('follow_user_id', follow_id), # 粉丝
        ]

        columns_to_get = []
        consumed, return_row, next_token = self.client.get_row(table_name, primary_key, columns_to_get)
        data = {}
        try:
            result = return_row.primary_key + return_row.attribute_columns
            for item in result:
                data[item[0]] = item[1]
        except:
            pass

        return data

    def focus_author(self,author_id, follow_id, focus):
        """关注作者"""
        table_name = "user_relation_table"
        # 2. 主键列
        primary_key = [
            ('user_id', author_id), # 作者
            ('follow_user_id', follow_id), # 粉丝
        ]
        if focus:
            """关注作者"""
            attribute_columns = [('timestamp', datetime.now().timestamp())]
            row = Row(primary_key, attribute_columns)
            consumed, return_row = self.client.put_row(table_name, row)
        else:
            """取关作者"""
            row = Row(primary_key)
            consumed, return_row = self.client.delete_row(table_name, row, None)

        return return_row

    def get_follow_list(self,author_id):
        """获取粉丝列表"""
        table_name = "user_relation_table"
        # 主键范围[起始范围]
        inclusive_start_primary_key = [
            ('user_id', author_id),
            ('follow_user_id', INF_MIN),
        ]
        # 主键范围[结束范围]
        exclusive_end_primary_key = [
            ('user_id', author_id),
            ('follow_user_id', INF_MAX),
        ]

        # 查询所有属性列
        columns_to_get = []  # 表示返回所有列

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name,  # 操作表明
            Direction.FORWARD,  # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
            inclusive_start_primary_key, exclusive_end_primary_key,  # 取值范围
            columns_to_get,  # 返回字段列
            max_version=1  # 返回版本数量
        )
        data = []
        if len(row_list) > 0:
            for row in row_list:
                row_data = row.primary_key + row.attribute_columns
                item_data = {}
                for item in row_data:
                    item_data[item[0]] = item[1]
                data.append(item_data)
        return data

    def push_feed(self, author_id, follow_list, article_id):
        """推送Feed流"""
        # 表名
        table_name = "user_message_table"
        put_row_items = []
        for follow in follow_list:
            # 主键列
            primary_key = [  # ('主键名', 值),
                ('user_id', follow['follow_user_id']),  # 接收Feed的用户ID
                ('sequence_id', PK_AUTO_INCR),  # 如果是自增主键，则值就是 PK_AUTO_INCR
                ("sender_id", author_id),  # 作者
                ("message_id", article_id),  # 文章
            ]
            # 属性列
            attribute_columns = [('recevice_time', datetime.now().timestamp()), ('is_read', False)]
            # 创建数据对象
            row = Row(primary_key, attribute_columns)
            # 如果数据存在，不报错
            item = PutRowItem(row, None)
            put_row_items.append(item)

        # 创建批量操作数据的请求对象
        request = BatchWriteRowRequest()
        request.add(TableInBatchWriteRowItem(table_name, put_row_items))
        # 发送请求操作
        result = self.client.batch_write_row(request)
        # 获取操作结果是否全部成功
        return result.is_all_succeed()

    def get_last_id(self,follow_id):
        """提取用户上一次拉去Feed流的最后主键"""
        table_name = "user_message_session_table"
        # 主键范围[起始范围]
        inclusive_start_primary_key = [
            ('user_id', follow_id),
            ('last_sequence_id', INF_MIN),
        ]
        # 主键范围[结束范围]
        exclusive_end_primary_key = [
            ('user_id', follow_id),
            ('last_sequence_id', INF_MAX),
        ]

        # 查询所有属性列
        columns_to_get = []  # 表示返回所有列
        limit=1
        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name,  # 操作表明
            Direction.FORWARD,  # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
            inclusive_start_primary_key, exclusive_end_primary_key,  # 取值范围
            columns_to_get,  # 返回字段列
            limit=1,
            max_version=1  # 返回版本数量
        )
        data = {}
        if len(row_list) > 0:
            row = row_list[0]
            row_data = row.primary_key + row.attribute_columns
            for item in row_data:
                data[item[0]] = item[1]
        return data

    def pull_feed(self, user_id, sequence_id=None,sender_id=None,message_id=None,limit=5):
        """拉取Feed流"""
        table_name = "user_message_table"
        # 主键范围[起始范围]
        if sequence_id is None:
            sequence_id = INF_MIN
            sender_id = INF_MIN
            message_id=INF_MIN

        inclusive_start_primary_key = [
            ('user_id', user_id),
            ('sequence_id', sequence_id),
            ('sender_id', sender_id),
            ('message_id', message_id),
        ]
        # 主键范围[结束范围]
        exclusive_end_primary_key = [
            ('user_id', user_id),
            ('sequence_id', INF_MAX),
            ('sender_id', INF_MAX),
            ('message_id', INF_MAX),
        ]

        # 查询所有属性列
        columns_to_get = []  # 表示返回所有列

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name,  # 操作表明
            Direction.FORWARD,  # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
            inclusive_start_primary_key, exclusive_end_primary_key,  # 取值范围
            columns_to_get,  # 返回字段列
            max_version=1,  # 返回版本数量
            limit=limit
        )

        data = []
        if len(row_list) > 0:
            for row in row_list:
                data.append(row.primary_key[3][1])
        return next_start_primary_key, data

    def update_last_id(self,user_id, next_start_primary_key,last_sequence_id=None):
        """更新未读池中的主键列"""
        # 表名
        table_name = "user_message_session_table"

        if next_start_primary_key is not None:
            if last_sequence_id is not None:
                """删除上一次的推送ID"""
                primary_key = [
                    ('user_id', user_id),
                    ('last_sequence_id', last_sequence_id),
                ]

                row = Row(primary_key)
                consumed, return_row = self.client.delete_row(table_name, row, None)

            last_id={}
            import json
            if next_start_primary_key is not None:
                ret = {}
                for item in next_start_primary_key:
                    ret[item[0]]=item[1]
                last_id = json.dumps(ret)
            else:
                last_id = json.dumps(last_id)
            # 增加新的主键
            primary_key = [
                ('user_id', user_id),  # 粉丝ID
                ('last_sequence_id', last_id ),
            ]

            attribute_columns = []
            row = Row(primary_key,attribute_columns)
            consumed, return_row = self.client.put_row(table_name, row)

            return return_row

    def get_last_article(self, user_id):
        """查询用户最近操作的文章列表"""
        table_name = "user_message_log_table"
        # 主键范围[起始范围]
        inclusive_start_primary_key = [
            ('user_id', user_id),
            ('message_id', INF_MIN),
        ]
        # 主键范围[结束范围]
        exclusive_end_primary_key = [
            ('user_id', user_id),
            ('message_id', INF_MAX),
        ]

        # 查询所有属性列
        columns_to_get = []  # 表示返回所有列
        # 返回结果的数量，这里最多只能设置90条
        limit = 10

        # 设置过滤器。[逻辑条件]
        cond = CompositeColumnCondition(LogicalOperator.OR)
        # cond.add_sub_condition(SingleColumnCondition("属性列名称", '条件值', "比较运算符"))
        last_time = datetime.now().timestamp() - 2*7*24*60*60
        cond.add_sub_condition(SingleColumnCondition("last_time", last_time, ComparatorType.GREATER_EQUAL))
        cond.add_sub_condition(SingleColumnCondition("is_read", 1, ComparatorType.EQUAL))

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name,  # 操作表明
            Direction.FORWARD,  # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
            inclusive_start_primary_key, exclusive_end_primary_key,  # 取值范围
            columns_to_get,  # 返回字段列
            limit=limit,
            column_filter=cond, # 属性列条件
            max_version=1  # 返回版本数量
        )

        data = []
        if len(row_list) > 0:
            for row in row_list:
                data.append(row.primary_key[1][1])
        return data

    def get_recomment_user(self,user_id, article_id_list):
        """根据文章获取到相同特征的用户"""
        user_list = self.get_user_by_message_id(article_id_list)
        # 计算用户的相似度并按高低排序
        user_list = self.calc_value_time(user_id, user_list)
        return user_list

    def calc_value_time(self,data_id, data_list):
        """计算指定值出现的频率"""
        data = {}
        for item in data_list:
            if item != data_id:
                if item in data:
                    data[item]+=1
                else:
                    data[item]=1

        # 按用户出现频率进行逆序排列
        data_list = []
        for key in sorted(data, key=data.__getitem__,reverse=True):
            data_list.append(key)
        return data_list[:10]

    def get_user_by_message_id(self,message_id_list):
        """获取最近操作过指定文章的所有用户"""
        table_name = "user_message_log_table"
        # 主键范围[起始范围]
        inclusive_start_primary_key = [
            ('user_id', INF_MIN),
            ('message_id', INF_MIN),
        ]
        # 主键范围[结束范围]
        exclusive_end_primary_key = [
            ('user_id', INF_MAX),
            ('message_id', INF_MAX),
        ]

        # 查询所有属性列
        columns_to_get = []  # 表示返回所有列
        # 返回结果的数量，这里最多只能设置90条
        limit = 10
        # 设置过滤器。[逻辑条件]
        cond = CompositeColumnCondition(LogicalOperator.AND)
        last_time = datetime.now().timestamp() - 2*7*24*60*60
        cond.add_sub_condition(SingleColumnCondition("last_time", last_time, ComparatorType.GREATER_EQUAL))
        cond.add_sub_condition(SingleColumnCondition("is_read", 1, ComparatorType.EQUAL))

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name,
            Direction.FORWARD,
            inclusive_start_primary_key, exclusive_end_primary_key,
            columns_to_get,
            limit=limit,
            column_filter=cond,  # 属性列条件
            max_version=1
        )

        data = []
        if len(row_list) > 0:
            for row in row_list:
                if row.primary_key[1][1] in message_id_list:
                    data.append(row.primary_key[0][1])
        return data

    def get_user_article(self,recomment_user_list,my_history_article):
        """基于协同过滤算法进行智能推荐"""
        # 获取每一个用户最近查看过的文章
        recomement_article_list=[]
        for user_id in recomment_user_list:
            recomement_article_list += self.get_last_article(user_id)

        # 过滤当前用户已经操作的文章
        data_list = []
        for article in recomement_article_list:
            if article not in my_history_article:
                data_list.append(article)

        # 获取到推荐的文章id列表
        data = {}
        for item in data_list:
            if item in data:
                data[item] += 1
            else:
                data[item] = 1
        # 按用户出现频率进行逆序排列
        data_list = []
        for key in sorted(data, key=data.__getitem__, reverse=True):
            data_list.append(key)
        return data_list[:10]

    def update_article_push_status(self,user_id,message_id_list):
        """批量更新推荐过的文章到操作日志中"""
        table_name = "user_message_log_table"
        put_row_items = []
        for message_id in message_id_list:
            # 主键列
            primary_key = [
                ('user_id', user_id),
                ('message_id', message_id),
            ]
            # 属性列
            attribute_columns = [('last_time', datetime.now().timestamp()), ('is_push', 1)]
            # 创建数据对象
            row = Row(primary_key, attribute_columns)
            # 如果数据存在，不报错
            item = PutRowItem(row, None)
            put_row_items.append(item)

        # 创建批量操作数据的请求对象
        request = BatchWriteRowRequest()
        request.add(TableInBatchWriteRowItem(table_name, put_row_items))
        # 发送请求操作
        result = self.client.batch_write_row(request)
        # 获取操作结果是否全部成功
        return result.is_all_succeed()

    def filter_article_list(self,user_id, feed_list):
        """过滤掉曾经被推送的文章"""
        for message_id in feed_list:
            ret = self.check_article_push_status(user_id, message_id)
            print("user_id=%s,message_id=%s,ret=%s" % (user_id,message_id,ret))
            if ret:
                feed_list.remove(message_id)
        return feed_list

    def check_article_push_status(self,user_id,message_id):
        table_name = "user_message_log_table"
        # 查询主键列[查询单条数据必须声明主键列作为主要条件]
        primary_key = [
            ('user_id', user_id),
            ('message_id', message_id),
        ]

        # 需要返回的属性列：。如果columns_to_get为[]，则返回所有属性列。
        columns_to_get = []

        consumed, return_row, next_token = self.client.get_row(table_name, primary_key, columns_to_get)

        data = {}
        attribute_columns = getattr(return_row,"attribute_columns",None)
        if attribute_columns is not None:
            for item in return_row.attribute_columns:
                data[item[0]] = item[1]
        print(data.get("is_push"),data.get("is_read"))
        return data.get("is_push") == 1 or data.get("is_read") == 1

    def update_article_read_status(self, user_id, message_id):
        """更新用户对于文章的阅读记录"""
        table_name = "user_message_log_table"

        # 2. 主键列
        primary_key = [
            ('user_id', user_id),
            ('message_id', message_id),
        ]

        # 3. 属性列[普通字段，可选]
        attribute_columns = [('recevice_time', datetime.now().timestamp()), ('is_read', 1)]
        row = Row(primary_key, attribute_columns)
        consumed, return_row = self.client.put_row(table_name, row)
        return return_row