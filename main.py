from utility import Utility

if __name__ == "__main__":
    u = Utility()
    redis = u.redis
    redis.setvalue(name="i",value='0')
    print(redis.getvalue("i"))
    my_dict = {"name:""indraneel"}
    u.publish(my_dict=my_dict)
    u.consume()
