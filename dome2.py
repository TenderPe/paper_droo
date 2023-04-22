# 创建EIR树
import pickle
import xlwt
import random
from My_experiment.eIRTreeNodeClass import EIRTreeNode
leaf_list = []
random.seed(2)

g = open('../MEC_server/mecServer_.txt', 'rb')
e = pickle.load(g)  #

length = len(e)
print('本来的e集合里面的MEC数量：',length)
# 在叶子结点层给定一个集合，计算集和的上下左右边界,还有能量的边界
def leaf_compute_boundary(node_list):

    length = len(node_list)
    min_x = node_list[0].get_x()
    min_y = node_list[0].get_y()
    max_x = node_list[0].get_x()
    max_y = node_list[0].get_y()
    min_e = node_list[0].get_energy()
    max_e = node_list[0].get_energy()
    total_x = 0
    total_y = 0
    for i in range(length):
        total_x += node_list[i].get_x()
        total_y += node_list[i].get_y()
        if node_list[i].get_x() < min_x:
            min_x = node_list[i].get_x()
        if node_list[i].get_x() > max_x:
            max_x = node_list[i].get_x()
        if node_list[i].get_y() < min_y:
            min_y = node_list[i].get_y()
        if node_list[i].get_y() > max_y:
            max_y = node_list[i].get_y()
        if node_list[i].get_energy() < min_e:
            min_e = node_list[i].get_energy()
        if node_list[i].get_energy() > max_e:
            max_e = node_list[i].get_energy()
    center_x = total_x / length
    center_y = total_y / length

    return min_x, max_x, min_y, max_y, min_e, max_e, center_x, center_y


index = random.randint(0, length-1)
print('选取的中心点',index)
center_node = e[index]

x = center_node.get_x()
y = center_node.get_y()

child_list = []
for i in range(length):
    # print(len(child_list))
    x_boolean = (e[i - len(child_list)].get_x() < (x + 1)) and (e[i - len(child_list)].get_x() > (x - 1))
    y_boolean = (e[i - len(child_list)].get_y() < (y + 1)) and (e[i - len(child_list)].get_y() > (y - 1))
    if x_boolean & y_boolean:
        child_list.append(e[i - len(child_list)])
        node = e.pop(i - len(child_list) + 1)
for i in child_list:
    print(i)
print('现在的e集合里面的MEC数量：',len(e))
min_x, max_x, min_y, max_y, min_e, max_e, center_x, center_y = leaf_compute_boundary(child_list)
print(min_x, max_x, min_y, max_y, min_e, max_e, center_x, center_y)
eir_node = EIRTreeNode([], None, min_x, max_x, min_y, max_y, min_e, max_e,
                           child_list, center_x, center_y, len(child_list))
print(eir_node)

leaf_list.append(eir_node)

