'''
docker build -f Dockerfile -t registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/juchao_base:v1 .
docker push registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/juchao_base:v1
sudo docker pull registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/juchao_base:v1
'''


'''
sudo docker run --log-opt max-size=10m --log-opt max-file=3 \
-itd --name jclive --env LOCAL=0 \
registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/juchao_base:v1 \
python livenews/juchao_livenews_spider.py
'''


'''
sudo docker run --log-opt max-size=10m --log-opt max-file=3 \
-itd --name ant --env LOCAL=0 \
registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/juchao_base:v1 \
python history_ant/his_task.py
'''


''' 
sudo docker run --log-opt max-size=10m --log-opt max-file=3 \
-itd --name ant_merge --env LOCAL=0 --env VPN=0 \
registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/juchao_base:v1 \
python scripts/trans_2tl.py
'''

'''guba 
sudo docker run --log-opt max-size=10m --log-opt max-file=3 \
-itd --name guba --env LOCAL=1  --env VPN=1 \
registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/juchao_base:v1 \
python middle_tables/guba_gener_demo.py
'''

'''news 
sudo docker run --log-opt max-size=10m --log-opt max-file=3 \
-itd --name news --env LOCAL=1  --env VPN=1 \
registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/juchao_base:v1 \
python middle_tables/news_gener_demo.py

'''

'''ann 
sudo docker run --log-opt max-size=10m --log-opt max-file=3 \
-itd --name ann --env LOCAL=1  --env VPN=1 \
registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/juchao_base:v1 \
python middle_tables/ann_gener_demo.py
'''

# TODO -v 做文件映射不重新 built + 做一个 python/shell 部署脚本

'''final2
sudo docker run --log-opt max-size=10m --log-opt max-file=3 \
-itd --name final2 --env LOCAL=0 --env VPN=0 \
registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/juchao_base:v1 \
python final_summary/final_2.py
'''


'''final1
sudo docker run --log-opt max-size=10m --log-opt max-file=3 \
-itd --name final1 --env LOCAL=0 --env VPN=0 \
registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/juchao_base:v1 \
python final_summary/final_sf_secu_announcement_detail.py
'''

'''final3 
sudo docker run --log-opt max-size=10m --log-opt max-file=3 \
-itd --name final3 --env LOCAL=0 --env VPN=0 --env RUN=1 \
registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/juchao_base:v1 \
python final_summary/final_3.py
'''


'''add 
sudo docker run --log-opt max-size=10m --log-opt max-file=3 \
-itd --name addprefix --env LOCAL=0 --env VPN=0 \
registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/juchao_base:v1 \
python scripts/add_prefix.py

'''
