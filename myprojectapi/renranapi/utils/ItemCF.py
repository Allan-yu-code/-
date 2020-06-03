import numpy

class ItemCF(object):
    """基于物品的协同推荐"""
    def __init__(self, users, items, allUserItemsStarList):
        self.users = users
        self.items = items
        self.allUserItemsStarList = allUserItemsStarList

    def converRow2Col(self):
        """
        行转列
        :return:
        """
        return numpy.array(self.allUserItemsStarList).transpose().tolist()


    def cal_two_mv_sim(self, item1Stars: list, item2Stars: list):
        """
        欧式距离计算两个文章之间的相似度
        :param item1Stars:
        :param item2Stars:
        :return:
        """
        return numpy.sqrt(((numpy.array(item1Stars) - numpy.array(item2Stars)) ** 2).sum())


    def cal_all_mv_sim(self):
        """
        计算所有文章之间的相似度
        :return:
        """
        resDic = {}
        tempList = self.converRow2Col()
        for i in range(0, len(tempList)):
            for j in range(i + 1, len(tempList)):
                resDic[str(i) + '-' + str(j)] = self.cal_two_mv_sim(tempList[i], tempList[j])
        return resDic


    def calrecommendMoive(self,username: str) -> list:
        """
        计算待推荐的文章
        :return:list
        """
        temp = {}
        items_sim_dic = self.cal_all_mv_sim()
        userindex = self.users.index(username)
        target_user_item_list = self.allUserItemsStarList[userindex]
        for i in range(0, len(target_user_item_list)):
            for j in range(i + 1, len(target_user_item_list)):
                if target_user_item_list[i] == 1 and target_user_item_list[j] == 0 and (items_sim_dic.get(str(i) + '-' + str(j)) != None or items_sim_dic.get(str(j) + '-' + str(i)) != None):
                    sim = items_sim_dic.get(str(i) + '-' + str(j)) if (
                                items_sim_dic.get(str(i) + '-' + str(j)) != None) else items_sim_dic.get(
                        str(j) + '-' + str(i))
                    temp[j] = sim
                elif target_user_item_list[i] == 0 and target_user_item_list[j] == 1 and (items_sim_dic.get(str(i) + '-' + str(j)) != None or items_sim_dic.get(str(j) + '-' + str(i)) != None):
                    sim = items_sim_dic.get(str(i) + '-' + str(j)) if (
                            items_sim_dic.get(str(i) + '-' + str(j)) != None) else items_sim_dic.get(
                        str(j) + '-' + str(i))
                    temp[i] = sim
        temp = sorted(temp.items(), key=lambda d: d[1])
        recommendlist = [self.items[i] for i, v in temp]
        print("待推荐列表：", recommendlist)
        return recommendlist

if __name__ == '__main__':
    # 用户列表
    users = ["张三", "李四", "王五", "小六", "田七"]

    # 物品列表
    items = ["文章1", "文章2", "文章3", "文章4", "文章5", "文章6", "文章7"]

    # 用户和物品的关系[点赞,赞赏,点击,收藏]
    allUserItemsStarList = [
        [1, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0],
        [1, 1, 0, 1, 0, 1, 1]
    ]
    cf = ItemCF(users, items, allUserItemsStarList)
    print("所有文章之间的相似度：%s" % cf.cal_all_mv_sim())

    cf.calrecommendMoive("张三")