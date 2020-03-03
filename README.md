# Attack Vectors

A repository to monitor attack vectors mentioned in the [billion-dollar disinformation campaign to reelect the president in 2020](https://www.theatlantic.com/magazine/archive/2020/03/the-2020-disinformation-war/605530/)

## Local Journalism

>Parscale has indicated that he plans to open up a new front in this war: local news. Last year, he said the campaign intends to train “swarms of surrogates” to undermine negative coverage from local TV stations and newspapers. Polls have long found that Americans across the political spectrum trust local news more than national media. If the campaign has its way, that trust will be eroded by November.

>Running parallel to this effort, some conservatives have been experimenting with a scheme to exploit the credibility of local journalism. Over the past few years, hundreds of websites with innocuous-sounding names like the Arizona Monitor and The Kalamazoo Times have begun popping up. At first glance, they look like regular publications, complete with community notices and coverage of schools. But look closer and you’ll find that there are often no mastheads, few if any bylines, and no addresses for local offices. Many of them are organs of Republican lobbying groups; others belong to a mysterious company called Locality Labs, which is run by a conservative activist in Illinois. Readers are given no indication that these sites have political agendas—which is precisely what makes them valuable.

This [NYT story goes into the details of Metric Media](https://www.nytimes.com/2019/10/21/us/michigan-metric-media-news.html), an organization responsible for many of these sites:

> Metric Media’s chief executive is Bradley Cameron, according to his online biography, which says he advises private equity investors in Silicon Valley, has been retained by conservative groups and served as senior adviser in the 1990s to the “Republican strategy leader in the U.S. House of Representatives.”

> Many if not all of the sites were registered on June 30 and updated on the same day in August, according to online domain records. The sites say they are operated by Locality Labs, a Delaware company affiliated with networks of local websites in Maryland and Illinois, according to The Lansing State Journal.

> On its website, Metric Media describes its reporting philosophy as providing “objective, data-driven information without inserting personal or political viewpoints and biases.” The company wrote that it plans to open thousands of similar sites nationwide.

Findings:

|domain|twitterFollowers|siteName|facebookUrl|awsOrigin|lat|lng|twitterUsername|itunesAppStoreUrl|twitterAccountCreatedAt|twitterUserId|twitterFollowing|twitterTweets|
|:-----|:---------------|:---------------|:------------|:-------|:----------|:--------|:-----|:-----|:--------|:----------------|:----------------------|:------------|
|louisianarecord.com|27490|Louisiana Record|https://www.facebook.com/LouisianaRecord/|52.7.148.177|30.9842977|-91.9623327|louisianarecord|https://itunes.apple.com/us/app/louisiana-record/id619088844|2010-10-13T21:58:46.000Z|202364607|23013|20433|
|wvrecord.com|3991|West Virginia Record|https://www.facebook.com/WVRecord|52.7.148.177|38.5976262|-80.4549026|wvrecord|https://itunes.apple.com/us/app/wv-record/id599538288|2009-11-19T11:38:43.000Z|91087040|329|11660|
|legalnewsline.com|1666|Legal Newsline|https://www.facebook.com/pages/Legal-Newsline/299588323424419|52.7.148.177|43.6961725|-79.4389309|legalnewsline|https://itunes.apple.com/us/app/legal-newsline/id603098697?mt=8|2009-11-02T03:30:54.000Z|86864211|559|16089|
|setexasrecord.com|1136|Southeast Texas Record|https://www.facebook.com/SETexasRecord/|52.7.148.177|30.063191|-94.134436|setexasrecord|https://itunes.apple.com/us/app/se-texas-record/id592747678|2009-11-19T11:37:11.000Z|91086820|1442|15399|
|cookcountyrecord.com|1114|Cook County Record|https://www.facebook.com/cookcountyrecord|52.7.148.177|41.7376587|-87.697554|CookRecord|https://itunes.apple.com/us/app/cook-county-record/id715265623?mt=8|2013-08-06T19:51:38.000Z|1651123645|408|12065|
|madisonrecord.com|757|Madison - St. Clair Record|https://www.facebook.com/pages/MadisonSt-Clair-Record/164779816968453|52.7.148.177|43.0730517|-89.4012302|madisonrecord|https://itunes.apple.com/us/app/madison-st-clair-record/id597238468?mt=8|2009-11-19T11:34:47.000Z|91086406|583|13633|
|lakecountygazette.com|533|Lake County Gazette|https://www.facebook.com/Lake-County-Gazette-854479238006224|35.170.88.147|39.0839644|-122.8084496|lakecntygazette||2015-11-17T00:59:16.000Z|4206041674|249|4132|
|kankakeetimes.com|487|Kankakee Times|https://www.facebook.com/kankakeetimes|35.170.88.147|41.1200325|-87.8611531|Kankakee_Times||2015-11-18T13:34:04.000Z|4218254801|244|2257|
|pennrecord.com|485|Pennsylvania Record|https://www.facebook.com/pages/Pennsylvania-Record/338776239487764|52.7.148.177|41.2033216|-77.1945247|pennrecord|https://itunes.apple.com/us/app/pennsylvania-record/id623294648|2011-05-16T13:28:41.000Z|299652000|219|7867|
|dupagepolicyjournal.com|444|Dupage Policy Journal|https://www.facebook.com/DuPage-Policy-Journal-440850842779072|35.170.88.147|41.8243831|-88.0900762|DupageJournal||2015-01-29T14:45:45.000Z|3001471430|260|5060|

[700+ more with 270+ Facebook pages, thousands of Facebook accounts and tens of thousands of Twitter followers](https://github.com/MassMove/AttackVectors/blob/master/LocalJournals/sites.csv).

Their shit looks really real: https://kalamazootimes.com until you start looking at all the articles at once: https://kalamazootimes.com/stories/tag/126-politics

Some quick Google-fu with a sentence from their about page:
https://www.google.com/search?q=%22Metric+Media+was+established+to+fill+the+void+in+community+news+after+years+of+decline+in+local+reporting+by+legacy+media.%22&rlz=1C1GCEU_nlNL823NL823&filter=0


[Shitty Google Maps plot](https://massmove.github.io/AttackVectors/LocalJournals/gmplot.html):

![2020 elections map](LocalJournals/gmplot.png?raw=true "US 2020 Elections Map")

[QGIS visualization with domain info](https://massmove.github.io/AttackVectors/LocalJournals/map.html):

![Local Journals Map](https://i.imgur.com/LP3SFEj.png "Local Journals Map")

[Interactive Heat Map](https://arcg.is/0KmXKK):

![Interactive Heat Map](https://i.imgur.com/TXO6xyN.png "Local Journals Heatmap")

## Legal Findings

https://www.fec.gov/files/legal/murs/7148/19044475209.pdf

[Legal Findings](https://github.com/MassMove/AttackVectors/blob/master/LocalJournals/LegalFindings.md)

## Twitter

>But when Twitter employees later reviewed the activity surrounding Kentucky’s election, they concluded that the bots were largely based in America—a sign that political operatives here were learning to mimic [foreign tactics].

From the Twitter Transparency Report:

| Date     | Country  | Msg Info  | Media | Accounts |
|:-----------|:-----------:|:------------:|:------------:|------------:|
| 201906|Catalonia |1.5 MB|2.74 GB|130 |
| 201906|Iran|316 MB|258 GB|1,666 |
| 201906|Iran|318 MB|183 GB|248 |
| 201906|Iran|46 MB|55 GB|2,865 |
| 201906|Russia|260 KB|72 MB|4|
| 201906|Venezuela |64 MB|24 GB|33 |
| 201906|China |158 MB|85 GB|744  |
| 201906|China |169 MB|40 GB|196 |
| 201906|China |913 MB|604 GB|4,301| 
| 201910|Saudi Arabia |4.3 GB|1.3 TB|5,929|

[12 more in the war room with further sources](https://www.reddit.com/r/MassMove/wiki/warroom)

## Websites resembling official campaigns

>Last year, a website resembling an official Biden campaign page appeared on the internet. It emphasized elements of the candidate’s legislative record likely to hurt him in the Democratic primary—opposition to same-sex marriage, support for the Iraq War—and featured video clips of his awkward encounters with women. The site quickly became one of the most-visited Biden-related sites on the web. It was designed by a Trump consultant.

Not much to report on this front yet. Scouts?

- [berniesander.com](http://berniesander.com/)
