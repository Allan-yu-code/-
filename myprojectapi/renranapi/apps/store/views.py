from rest_framework.views import APIView
from rest_framework.response import Response
# from tablestore import OTSClient,PK_AUTO_INCR,TableMeta,TableOptions,ReservedThroughput,CapacityUnit
from tablestore import *
from django.conf import settings
class TableAPIView(APIView):
    """表操作"""
    @property
    def client(self):
        return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    def post(self,request):
        """创建数据表"""
        # 表名
        table_name = "user_message_table"

        # 设置主键
        # schema_of_primary_key = [
        # ('字段名', '字段类型'),  # 第一个主键默认是分区间，不能是浮点数类型，而且不能设置自增
        # ('字段名', '字段类型', PK_AUTO_INCR), # 其他主键如果要设置为自增，则在第三个成员中声明
        # ...
        # ]

        schema_of_primary_key = [
            ('user_id', 'INTEGER'),
            ('sequence_id', 'INTEGER', PK_AUTO_INCR),
            ("sender_id", 'INTEGER'),
            ("message_id", 'INTEGER')
        ]

        # 设置表的元信息
        table_meta = TableMeta(table_name, schema_of_primary_key)
        # 设置数据的有效期
        table_option = TableOptions(7*86400, 5)
        # 设置数据的预留读写吞吐量
        reserved_throughput = ReservedThroughput(CapacityUnit(0, 0))
        # 创建数据
        self.client.create_table(table_meta, table_option, reserved_throughput)

        return Response({"message":"ok"})

    def delete(self, request):
        """删除表"""
        table = "user_message_table"
        self.client.delete_table(table)
        return Response({"message": "ok"})

    def get(self,request):
        """列出所有的表"""
        table_list = self.client.list_table()
        data = []
        for table in table_list:
            data.append(table)

        return Response(data)

from django.utils import timezone as datetime
from tablestore import Row
class DataAPIView(APIView):
    @property
    def client(self):
        return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    def post(self, rquest):
        """添加数据到表格中"""
        # 1. 表名
        table_name = "user_message_table"

        # 2. 主键列
        primary_key = [
            # ('主键名', 值),
            ('user_id', 3), # 接收Feed的用户ID
            ('sequence_id', PK_AUTO_INCR), # 如果是自增主键，则值就是 PK_AUTO_INCR
            ("sender_id",1), # 发布Feed的用户ID
            ("message_id",4), # 文章ID
        ]

        # 3. 属性列[普通字段，可选]
        attribute_columns = [('recevice_time', datetime.now().timestamp()), ('read_status', False)]
        row = Row(primary_key, attribute_columns)
        consumed, return_row = self.client.put_row(table_name, row)
        print(return_row)

        return Response({"message": "ok"})

    def get(self,request):
        """获取指定数据"""
        # 表名
        table_name = "user_message_table"
        # 查询主键列[查询单条数据必须声明主键列作为主要条件]
        primary_key = [
            ('user_id', 3),
            ('sequence_id', 1587177576116000), # 自增主键，需要自己到阿里云上面查看补充进来以后测试
            ("sender_id", 1),
            ("message_id", 4)
        ]

        # 需要返回的属性列：。如果columns_to_get为[]，则返回所有属性列。
        columns_to_get = []
        # columns_to_get = ['recevice_time', 'read_status', 'age', 'sex']

        consumed, return_row, next_token = self.client.get_row(table_name, primary_key, columns_to_get)
        print(return_row) # <tablestore.metadata.Row object at 0x7f15399ef470>
        print(return_row.primary_key) # [('user_id', 3), ('sequence_id', 1587177576116000), ('sender_id', 1), ('message_id', 4)]
        print(return_row.attribute_columns) # [('read_status', False, 1587177576116), ('recevice_time', 1587177575.620502, 1587177576116)]

        return Response({"message": "ok"})

    def delete(self,request):
        """删除指定一条数据"""
        # 表名
        table_name = "user_message_table"
        # 主键列
        primary_key = [
            ('user_id', 3),
            ('sequence_id', 1587178196943000),
            ("sender_id", 1),
            ("message_id", 4)
        ]

        row = Row(primary_key)
        # 没有报错，则表示删除成功
        consumed, return_row = self.client.delete_row(table_name, row, None)
        return Response({"message":"ok"})

from tablestore import INF_MAX,INF_MIN,CompositeColumnCondition,LogicalOperator,SingleColumnCondition,ComparatorType,Direction,Condition,RowExistenceExpectation,PutRowItem,BatchWriteRowRequest,TableInBatchWriteRowItem
class RowAPIView(APIView):
    @property
    def client(self):
        return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    def get(self,request):
        """按主键范围获取多行数据"""
        # 表名
        table_name = "user_message_table"
        # 主键范围[起始范围]
        inclusive_start_primary_key = [
            ('user_id', 3),
            ('sequence_id', INF_MIN),
            ('sender_id', INF_MIN),
            ('message_id', INF_MIN)
        ]
        # 主键范围[结束范围]
        exclusive_end_primary_key = [
            ('user_id', 3),
            ('sequence_id', INF_MAX),
            ('sender_id', INF_MAX),
            ('message_id', INF_MAX)
        ]

        # 查询所有属性列
        columns_to_get = []  # 表示返回所有列
        # 返回结果数据量
        limit = 5

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name,  # 操作表明
            Direction.FORWARD,  # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
            inclusive_start_primary_key, exclusive_end_primary_key,  # 取值范围
            columns_to_get,  # 返回字段列
            limit,  # 结果数量
            # column_filter=cond, # 条件
            max_version=1  # 返回版本数量
        )

        print("一共返回了：%s" % len(row_list))

        if len(row_list)>0:
            for row in row_list:
                print(row.primary_key, row.attribute_columns)

        # next_start_primary_key　表示 下一页查询数据的开始位置

        return Response({"message": next_start_primary_key})

    def post(self,request):
        """添加多条数据"""
        # 表名
        table_name = "user_message_table"

        # 要批量操作的数据对象
        put_row_items = []

        for i in [3,5,10,6,17]:
            # 主键列
            primary_key = [  # ('主键名', 值),
                ('user_id', i),  # 接收Feed的用户ID
                ('sequence_id', PK_AUTO_INCR),  # 如果是自增主键，则值就是 PK_AUTO_INCR
                ("sender_id", 1),  # 发布Feed的用户ID
                ("message_id", 9),  # 文章ID
            ]
            # 属性列
            attribute_columns = [('recevice_time', datetime.now().timestamp()), ('read_status', False)]
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
        print(result.is_all_succeed())

        return Response({"message": "ok"})