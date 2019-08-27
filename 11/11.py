import json

def main():
    mydict = {
        'name':'lh',
        'age':38,
        'qq':957658,
        'friends':['wdc','byf'],
        'cars':[
            {'brand':'byd','max_speed':180},
            {'brand':'audi','max_speed':280},
            {'brand':'benz','max_speed':320}
        ]
    }
    try:
        with open('data.json','w',encoding='utf-8') as fs:
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    print('保存数据完成')

if __name__ == '__main__':
    main()