'''公告重大事件汇总表
CREATE TABLE `sf_secu_announcement_summary` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `InnerCode` int(10) DEFAULT NULL COMMENT '股票内部编码',
  `SecuCode` varchar(100) NOT NULL COMMENT '股票代码',
  `TradeDate` datetime NOT NULL COMMENT '日期',
  `Sentiment` tinyint(4) NOT NULL COMMENT '情感倾向标签(重大事件)(显示颜色)',
  `EventCode` varchar(100) NOT NULL COMMENT '公告事件类型（显示标签名称）',
  `AnnID` bigint(20) NOT NULL COMMENT '公告基础表中的ID字段',
  `AnnTitle` varchar(1000) DEFAULT NULL COMMENT '公告标题',
  `Website` varchar(200) DEFAULT NULL COMMENT '网址',
  `IfShow` tinyint(4) NOT NULL DEFAULT 1 COMMENT '是否软件展示(1-展示，0-不展示)',
  `CreateTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `UpdateTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `un1` (`SecuCode`,`TradeDate`,`EventCode`),
  KEY `k1` (`SecuCode`,`TradeDate`,`Sentiment`,`EventCode`,`IfShow`,`UpdateTime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='股票-公告重大事件汇总表';


SecuCode, InnerCode : 从 dc_ann_event_source_ann_detail 中的 SecuCode 生成;
TradeDate: 从 dc_ann_event_source_ann_detail 中的 PubTime 可生成;
生成规则: 如果公告的发布时间为交易日，则使用这一天。
如果不是, 则使用之前最近的一个交易日。
用到的表 tradingday

Sentiment: 用 dc_ann_event_source_ann_detail 中的 EventCode 与 sf_const_announcement 关联取其中的 Sentiment ;
EventCode: dc_ann_event_source_ann_detail 中的 EventCode;
AnnID: dc_ann_event_source_ann_detail 中的 AnnID ;
AnnTitle : dc_ann_event_source_ann_detail 中的 Title  ;
Website: dc_ann_event_source_ann_detail 中的 PDFLink ;
'''
import datetime
import sys

from base_spider import SpiderBase


class FinalAntSummary(SpiderBase):
    def __init__(self, start_time: datetime.datetime, end_time: datetime.datetime):
        super(FinalAntSummary, self).__init__()
        self.source_table = 'dc_ann_event_source_ann_detail'
        self.target_table = 'sf_secu_announcement_summary'
        self.tool_table = "secumain"

        self.start_time = start_time
        self.end_time = end_time
        self.codes_map = {}

    def get_inner_code_map(self):
        self._yuqing_init()
        sql = '''select SecuCode, InnerCode from {} where SecuCode in (select distinct(SecuCode) from {}); '''.format(
            self.tool_table, self.source_table,
        )
        ret = self.yuqing_client.select_all(sql)
        for r in ret:
            self.codes_map[r.get('SecuCode')] = r.get('InnerCode')

    def launch(self):
        self.get_inner_code_map()

        sql = '''select AnnID, SecuCode, PubTime, EventCode, Title, PDFLink from {} where PubTime  between '{}' and '{}'; '''.format(
            self.source_table, datetime.datetime(2020, 7, 30), datetime.datetime(2020, 10, 30))
        self._yuqing_init()
        datas = self.yuqing_client.select_all(sql)
        for data in datas:
            print(data)
            ann_id = data.get("AnnID")
            pub_time = data.get("PubTime")

            secu_code = data.get("SecuCode")
            inner_code = self.codes_map.get(secu_code)



            print(secu_code, inner_code)

            sys.exit(0)


if __name__ == '__main__':
    FinalAntSummary(datetime.datetime(2020, 7, 30), datetime.datetime(2020, 10, 30)).launch()
    # FinalAntSummary(datetime.datetime(2020, 7, 30), datetime.datetime(2020, 10, 30)).get_inner_code_map()