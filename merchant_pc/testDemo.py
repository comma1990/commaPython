# getCookie方法提取，所有方法必须传cookie字段
import xlrd
import merchant_pc.create_roles, merchant_pc.createProduct
import openpyxl

if __name__ == '__main__':
    # 获取cookie
    from merchant_pc.getCookie import getCookies

    Cookie = getCookies()

    # 获取仓库名
    # from merchant_pc.getDepot import getDepot
    # getDepot(Cookie)

    # #from merchant_pc.create_roles import create_yaoqingkefu
    # '''创建客服专员'''
    # merchant_pc.create_roles.create_kefuzhuguan(Cookie)
    # '''创建邀请专员'''
    # merchant_pc.create_roles.create_yaoqingkefu(Cookie)
    # '''创建高级管理员'''
    # merchant_pc.create_roles.create_gaojiguanliyuan(Cookie)
    # '''普通管理员'''
    # merchant_pc.create_roles.create_putongguanliyuan(Cookie)
    # '''创建客服主管'''
    # merchant_pc.create_roles.create_kefuzhuguan(Cookie)
    # '''创建发货专员和仓库管理员'''
    # merchant_pc.create_roles.create_fahuohecangkuguanliyuan(Cookie)
    # '''创建销售专员'''
    # merchant_pc.create_roles.create_xiaoshouzhuanyuan(Cookie)
    # '''创建商品管理员'''
    # merchant_pc.create_roles.create_shangpingguanliyuan(Cookie)
    # '''创建财务'''
    # merchant_pc.create_roles.create_caiwu(Cookie)
    # '''创建美工'''
    # merchant_pc.create_roles.create_meigong(Cookie)
    # '''创建直播专员'''
    # merchant_pc.create_roles.create_zhibozhuanyuan(Cookie)

    # '''创建商品,循环创建'''
    # wk = xlrd.open_workbook('D:\python\study\中免商品信息.xlsx')
    # sheet = wk.sheets()[1]
    # x = int(input('请输入你想从第几张图片开始创建商品：'))
    # if x>sheet.nrows:
    #     print('商品图片数量不足！！！')
    # else:
    #
    #     n = int(input('请输入要创建的商品数量：'))
    #     if n > sheet.nrows - x:
    #         print('商品图片数量不足！')
    #     else:
    #         for item in range(n):
    #             pic = sheet.col_values(6, x, x + 1)     # 从表中索引为6列取值，值的返回是x行到x+1行
    #             merchant_pc.createProduct.createProduct(Cookie, pic)
    #             x += 1

    # 创建优惠券
    # from merchant_pc.createCoupon import createCoupon
    # createCoupon(Cookie)

    # 获取商品列表
    # from merchant_pc.getProductId import getProductId
    # getProductId(Cookie)
