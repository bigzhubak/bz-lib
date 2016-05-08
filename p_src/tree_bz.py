#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
生成树状结构
'''
from public_bz import storage

def makeTreeByName(nodes, name, parent, start_name_value=''):
    '''
    create by bigzhu at 16/04/28 15:23:07 根据指定的字段来将铺平的数据组织成树状
    name: 身份标记字段名
    parent: 父身份标记字段名
    start_name_value: 从哪个节点以下开始
    '''
    tree = []
    # 为了确定节点所在层，使用parent_id进行排序
    nodes = sorted(nodes, key=lambda k: k[name])
    for node in nodes:
        if node[parent] == start_name_value:
            tree.append(node)
        else:
            parent_node = findNodeByName(tree, name, node[name])
            if parent_node:
                addChilren(parent_node, node)
            # 父节点还没加入到 tree 中
            else:
                parent_node = findNodeByName(nodes, name, node[parent])
                if parent_node:
                    addChilren(parent_node, node)
    return tree

def findNodeByName(nodes, name, key):
    '''
    在树里面查找节点
    '''
    for node in nodes:
        if node[name] == key:
            return node
        # 递归查找其子节点
        if node.get('children'):
            target_node = findNodeByName(node.children, name, key)
            if target_node:
                return target_node




def makeTree(nodes, parent_id=0):
    '''
    node.id = 0
    node.parent_id = 0
    node.children = []

    根据 node.id 和 node.parent_id 将铺平的数据组织成树状
    放到 children 节点
    '''
    tree = []
    # 为了确定节点所在层，使用parent_id进行排序
    nodes = sorted(nodes, key=lambda k: k.parent_id)
    for node in nodes:
        if node.parent_id == parent_id:
            tree.append(node)
        else:
            parent_node = findNode(tree, node.parent_id)
            if parent_node:
                addChilren(parent_node, node)
            # 父节点还没加入到 tree 中
            else:
                parent_node = findNode(nodes, node.parent_id)
                if parent_node:
                    addChilren(parent_node, node)
                #else:
                #    print 'parent_id= %s not found parent' % node.parent_id
    return tree


def addChilren(parent_node, child_node):
    '''
    加入子节点
    '''
    if parent_node.get('children'):
        parent_node.children.append(child_node)
    else:
        parent_node.children = [child_node]


def findNode(nodes, id):
    '''
    在树里面查找节点
    '''
    for node in nodes:
        if node.id == id:
            return node
        # 递归查找其子节点
        if node.get('children'):
            target_node = findNode(node.children, id)
            if target_node:
                return target_node


def makeSelectTree(nodes):
    '''
    '''
    tree = []
    for node in nodes:
        if node.parent_id == 0:
            tree.append(node)
        else:
            parent_node = findSelectNode(tree, node.parent_id)
            if parent_node:
                addSelectChilren(parent_node, node)
            # 父节点还没加入到 tree 中
            else:
                parent_node = findSelectNode(nodes, node.parent_id)
                addSelectChilren(parent_node, node)
    return tree


def addSelectChilren(parent_node, child_node):
    '''
    加入子节点
    '''
    parent_id = str(parent_node.get('id'))
    if parent_node.get(parent_id):
        parent_node[parent_id].append(child_node)
    else:
        parent_node[parent_id] = [child_node]


def findSelectNode(nodes, id):
    '''
    在树里面查找节点
    '''
    for node in nodes:
        if node.id == id:
            return node
        # 递归查找其子节点
        if node.get(str(id)):
            target_node = findSelectNode(node[str(id)], id)
            if target_node:
                return target_node


def findParent(nodes, parent_id):
    '''
    查找ID的父元素
    create by liuyong at 15/06/08 14:55:33
    '''
    for node in nodes:
        if node.id == parent_id:
            return node


def findParentList(nodes, parent_id):
    '''
    查找元素的所有父元素
    create by liuyong at 15/06/08 14:55:53
    '''
    ParentList = []
    node = findParent(nodes, parent_id)
    while node:
        #ParentList.append(node)
        ParentList.insert(0, node)
        node = findParent(nodes, node.parent_id)
    return ParentList


if __name__ == '__main__':
    nodes = []

    node = storage()
    node.id = 3
    node.parent_id = 2
    nodes.append(node)

    node = storage()
    node.id = 2
    node.parent_id = 1
    nodes.append(node)

    node = storage()
    node.id = 5
    node.parent_id = 1
    nodes.append(node)

    node = storage()
    node.id = 1
    node.parent_id = 0
    nodes.append(node)

    node = storage()
    node.id = 8
    node.parent_id = 0
    nodes.append(node)

    node = storage()
    node.id = 9
    node.parent_id = 8
    nodes.append(node)
    #print makeTree(nodes)
    print findParentList(nodes, 2)
