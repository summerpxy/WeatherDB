import dbflow
import spider

if __name__ == '__main__':
    names = dbflow.get_location_info_by_xlsx()
    print(len(names))
    name, ad_code, city_code = names[80]
    print(name)
    text = spider.get_city_w_id(name)
    print("result:" + text)
