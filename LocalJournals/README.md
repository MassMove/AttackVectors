# Attack Vectors

A repository to monitor attack vectors mentioned in the [billion-dollar disinformation campaign to reelect the president in 2020](https://www.theatlantic.com/magazine/archive/2020/03/the-2020-disinformation-war/605530/)

## Local Journals

>Running parallel to this effort, some conservatives have been experimenting with a [scheme to exploit the credibility of local journalism](https://www.nytimes.com/2019/10/31/upshot/fake-local-news.html). Over the past few years, hundreds of websites with innocuous-sounding names like the Arizona Monitor and The Kalamazoo Times have begun popping up. [At first glance, they look like regular publications, complete with community notices and coverage of schools](https://www.cjr.org/tow_center_reports/hundreds-of-pink-slime-local-news-outlets-are-distributing-algorithmic-stories-conservative-talking-points.php). But look closer and you’ll find that there are often no mastheads, few if any bylines, and no addresses for local offices. Many of them are organs of Republican lobbying groups; others belong to a mysterious company called Locality Labs, which is run by a conservative activist in Illinois. Readers are given no indication that these sites have political agendas—which is precisely what makes them valuable.

Their stuff looks really real: https://kalamazootimes.com until you start looking at all the articles at once: https://kalamazootimes.com/stories/tag/126-politics

### Maps

Some maps to relay the sheer magnitude of the operation with over a thousand domains operating as fake local journals:

[QGIS visualization with domain info](https://massmove.github.io/AttackVectors/LocalJournals/map.html):

![Local Journals Map](https://i.imgur.com/LP3SFEj.png "Local Journals Map")

[Interactive Heat Map](https://arcg.is/0KmXKK):

![Interactive Heat Map](https://i.imgur.com/TXO6xyN.png "Local Journals Heatmap")

### Domains

|domain|twitterFollowers|siteName|facebookUrl|awsOrigin|lat|lng|twitterUsername|twitterAccountCreatedAt|twitterUserId|twitterFollowing|twitterTweets|
|:-----|:---------------|:---------------|:------------|:-------|:----------|:--------|:-----|:-----|:----------------|:----------------------|:------------|
|louisianarecord.com|27490|Louisiana Record|https://www.facebook.com/LouisianaRecord/|52.7.148.177|30.9842977|-91.9623327|louisianarecord|2010-10-13T21:58:46.000Z|202364607|23013|20433|
|wvrecord.com|3991|West Virginia Record|https://www.facebook.com/WVRecord|52.7.148.177|38.5976262|-80.4549026|wvrecord|2009-11-19T11:38:43.000Z|91087040|329|11660|
|legalnewsline.com|1666|Legal Newsline|https://www.facebook.com/pages/Legal-Newsline/299588323424419|52.7.148.177|43.6961725|-79.4389309|legalnewsline|2009-11-02T03:30:54.000Z|86864211|559|16089|
|setexasrecord.com|1136|Southeast Texas Record|https://www.facebook.com/SETexasRecord/|52.7.148.177|30.063191|-94.134436|setexasrecord|2009-11-19T11:37:11.000Z|91086820|1442|15399|
|cookcountyrecord.com|1114|Cook County Record|https://www.facebook.com/cookcountyrecord|52.7.148.177|41.7376587|-87.697554|CookRecord|2013-08-06T19:51:38.000Z|1651123645|408|12065|
|madisonrecord.com|757|Madison - St. Clair Record|https://www.facebook.com/pages/MadisonSt-Clair-Record/164779816968453|52.7.148.177|43.0730517|-89.4012302|madisonrecord|2009-11-19T11:34:47.000Z|91086406|583|13633|
|lakecountygazette.com|533|Lake County Gazette|https://www.facebook.com/Lake-County-Gazette-854479238006224|35.170.88.147|39.0839644|-122.8084496|lakecntygazette|2015-11-17T00:59:16.000Z|4206041674|249|4132|
|kankakeetimes.com|487|Kankakee Times|https://www.facebook.com/kankakeetimes|35.170.88.147|41.1200325|-87.8611531|Kankakee_Times|2015-11-18T13:34:04.000Z|4218254801|244|2257|
|pennrecord.com|485|Pennsylvania Record|https://www.facebook.com/pages/Pennsylvania-Record/338776239487764|52.7.148.177|41.2033216|-77.1945247|pennrecord|2011-05-16T13:28:41.000Z|299652000|219|7867|
|dupagepolicyjournal.com|444|Dupage Policy Journal|https://www.facebook.com/DuPage-Policy-Journal-440850842779072|35.170.88.147|41.8243831|-88.0900762|DupageJournal|2015-01-29T14:45:45.000Z|3001471430|260|5060|
|**[1000+ more in sites.csv](https://github.com/MassMove/AttackVectors/blob/master/LocalJournals/sites.csv)**||||||||||||

### Anti-Virus

#### Twitter Bot

A Twitter bot to monitor and respond to tweets promoting state-backed information operations is at https://github.com/karan/TakeoverBot. It downloads fake local news sites.csv file, searches for mentions of each on Twitter, and replies to them with an informative message.

#### Reddit Bot

A Reddit bot to inform users when they post a link to one of the local journals: https://github.com/MassMove/AttackVectors/blob/master/LocalJournals/utils/CyberDome/tron.py.

#### Reddit Post Monitor

A script that lists when domains were last posted to reddit in the last month: https://github.com/MassMove/AttackVectors/tree/master/LocalJournals/utils/RedditPostMonitor.

#### uBlock Origin Filters

uBlock Origin can be configured to alert us when one of the local journals appears in the wild. Open the configuration dashboard and tab to "My filters" or enter this URL in Chrome: [chrome-extension://cjpalhdlnbpafiamejdnhcphjbkeiagm/dashboard.html#1p-filters.html](chrome-extension://cjpalhdlnbpafiamejdnhcphjbkeiagm/dashboard.html#1p-filters.html).

    ||kalamazootimes.com

Get the rest here: https://github.com/MassMove/AttackVectors/blob/master/LocalJournals/sites-ublock-origin-filter.md

#### Reddit Enhancement Suite

RES can also be configured to alert us... in Appearance, go to Stylesheet Loader and add a row like:

    .title[href*="kalamazootimes.com"]:before { content: "PROPAGANDA"; color: white; background-color: red; border: 2px solid #000; }

Get the rest here: https://github.com/MassMove/AttackVectors/blob/master/LocalJournals/sites-reddit-enhancement-suite.md

### Methods

The methods used to find more domains are detailed in the [pull requests](https://github.com/MassMove/AttackVectors/pulls?q=is%3Apr+sort%3Acreated-asc+) - spme highlights:

- We started with basic Google-fu using a sentence from their about page: https://www.google.com/search?q=%22Metric+Media+was+established+to+fill+the+void+in+community+news+after+years+of+decline+in+local+reporting+by+legacy+media.%22 (click on: "repeat the search with the omitted results included")

- Dumped domains hosted by same servers on AWS

- crawled sites + relationships data set

- Reverse IP lookup

- Google BigQuery searches through 100s of TB in the HTTP Archive project for Google Analytics tags, Facebook pixels, and Quantserv IDs: https://discuss.httparchive.org/t/http-archive-project-vs-state-backed-disinformation-operations/1887

### Legal Findings

https://www.fec.gov/files/legal/murs/7148/19044475209.pdf

[Legal Findings](https://github.com/MassMove/AttackVectors/blob/master/LocalJournals/LegalFindings.md)

## Facebook

Facebook is raking in tens of thousands of dollars from ad campaigns paid for by LGIS (Local Government Information Services) to promote the various local journals:

- https://www.facebook.com/ads/library/?active_status=active&ad_type=political_and_issue_ads&country=US&impression_search_field=has_impressions_lifetime&q=lgis&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped

- https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=US&impression_search_field=has_impressions_lifetime&view_all_page_id=440850842779072

## Twitter

Twitter has suspended most of their accounts: https://twitter.com/DupageJournal