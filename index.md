# Location Bias in YouTube's Search Engine
*Does the YouTube search ranking algorithm reflect national geopolitics?*

* [Introduction](#introduction)
* [Literature review and approach](#literature-review-and-approach)
* [Methodology](#methodology)
* [Results](#results)
* [Project scope](#scope)
* [References](#references)

## Introduction

Algorithms are complex processes, and there exists limited understanding amongst the scholars and laymen alike about its functioning and implications, and its increasingly dominant role in the information we consume ‘can lead to a distortion of our perception’ (Rieder et al., 2018). In particular, the intermingling of algorithms with the political context, on social media platforms, such as YouTube, leads to real-world consequences, hence the call for developing a deeper understanding of the same, mainly along the lines of transparency and accountability. Our study aims to gather evidence about the growing speculation surrounding YouTube and its recommendation algorithms, and the extent to which it may be contributing to the ‘distortion of the perceptions’ of people through the promotion of extreme viewpoints and misinformation having geopolitical implications (Bryant, 2020). This further highlights the threat of ‘supercharged possibilities for sharp power’ looming large as the algorithms on social media platforms can potentially manipulate the public sentiment through computational propaganda, disinformation, and conspiracism by foreign actors and their domestic proxies (Miailhe, 2018). In this study, we explore the biases in search results of YouTube surrounding the controversy related to the Xinjiang region in China, and the Uighurs, a Muslim minority community, mainly to identify the relation (if any) between search results and geopolitical stance of the respective countries. Following the ‘scraping approach’, we aim to observe how YouTube’s socio-algorithmic functionings vary in different geolocations, by focusing on the retrieval and ranking of videos (Rieder et al., 2018). 

## Literature review and approach

We are philosophically inspired to probe the relationship between geopolitics and algorithms owned by private companies following the conceptualization of “liquid surveillance”, proposed by sociologist Zygmunt Bauman. He argues that previously solid distinctions between the government and the private sector, as well as between producers and consumers are converging, and thus should not be regarded as separate entities with diverging interests (Bauman& Lyon, 2012). Algorithms are a perfect manifestation of this, as they are more than just random steps of procedures expressed mathematically, but rather complex processes interlinked with cultural, political, social and economic flows.

As such, power relations embedded into the algorithm-driven search engines have been scrutinized ever since their popularization, with particular attention paid to hierarchization processes (Introna and Nissenbaum, 2000). Due to sheer mass of information on the internet, the search feature plays a crucial role in curating its messages, most prominently through ranking. Ranking attributes relevancy by implying that some content deserves more visibility than others, thus making it an influential element in the diffusion of information that informs user behavior (Shifman, 2013). Because of that, Youtube’s recommendation system was used to understand the role algorithms play in the creation of problematic communities, with studies finding that Youtube recommendation algorithm “fosters the formation of highly homophilous communities” (Kaiser& Rauchfleisch, 2020. This particularly matters in the context of rising far-right extremism, due to the potential of disastrous real life consequences and discrimination (Edelman and Luca, 2014). Yet, contrary to much of alarming literature on the “alt-right rabbit hole” (Ribeiro, 2019; Bryant, 2020), many audits argue that the agency of algorithms is overblown and doesn’t hold up to empirical scrutiny (Hussein et al., 2020; Munger&Phillips, 2020; Ledwich&Zaitsev, 2020). A fruitful theoretical distinction is made between “filter bubbles”as algorithmically induced and “echo-chambers” as voluntarily induced by the users (Kaiser& Rauchfleisch, 2020). For our purposes, we will not weigh in on the “algorithmic agency” debate and instead focus on the end results it produces. Regardless of their origin, homophilous algorithmic communities have been proven to form within countries. Additionally, they have also been shown to take into account national contexts that make “terms, language, and location” strong determining factors (Bozdag et al. 2014). Therefore, we ultimately aim to test the filter hypothesis on the international scale, seeking traces of geopolitical positions being reflected in Youtube’s search and ranking system. United States and China, as the two largest competing investors in AI and machine learning with the most coherent national strategies make for promising test subjects, because we expect their influence (if any) to be most saliently pronounced. Given Google’s secrecy around its algorithms to protect its business model, we employ a “scraping” approach (Sandvig et al., 2014) in order to analyze what the algorithm does, with the hopes of better understanding of how it does it, as well as the broader concerns of power and agency flows involved. 

## Methodology

a) To investigate biases in YouTube search results, a topic that held certain contention on a global scale had to be selected to evaluate geopolitical biases. The topic of Xinjiang and surrounding controversy related to China’s actions in the area and Muslim minority inhabitants was selected. The search was narrowed to three particular terms, “Xinjiang”, “Xinjiang Terrorism” and “Xinjiang Uighurs” and the top 20 results for each of these search terms would be collected for evaluation.

b) To understand the geopolitical impacts, a list of countries that had formally condemned China's actions in the Xinjiang region were compiled, along with countries that supported the actions as well as those who held a neutral stance. From this extensive list, five countries for each category (condemned, supported and neutral) were selected based on ease of access with respect to IP address availability on private VPN services. The list thus consisted of Germany, Netherlands, Spain, France and United States of America under nations that had condemned China, Venezuela, Egypt, Pakistan, Bangladesh and Philippines under nations that support China’s actions and finally, Italy, Mexico, Israel, India and South Korea under the neutral category.

c) A scraping script is run on python to collect data (URL and title) under each search term and append onto an excel sheet, resulting in 60 results for each country. The IP address is manually selected via VPN services (NordVPN and ExpressVPN) for each country and to ensure unbiased search results, the script opens Chrome under a YouTube account that is not signed in. Each video is then evaluated and the stance of the video, whether it was pro-china, critical, balanced or unrelated is entered in a separate column.  

d) Data visualization took steps to identify any biases in search terms by exploring multiple avenues. Density plots of the videos based on their stance is evaluated both by exploring based on specific search terms as well as irrespective of them. To run a linear regression, the stance of the video is made into a dummy variable for each category and divided by the rank to form weights to the results based on the order in which they appear. A combination of density plots, value counts on video titles and regression outputs forms the study’s conclusion. 

## Results

Let's begin by getting an overall impression of the data collected.
<br/><br/>
<div align="center"><img src='https://Krokke.github.io/Decoding-Biases-in-AI/images/map_pol_all.png' width='100%'></div>  
<div align="center"><u>Geopolitical attitudes towards China's treatment of Uighurs in Xinjiang, 2020. In red, nations that have condemned China; in green, nations that have supported it.</u></div>
<br>
This map clearly shows the divide between West and the Golbal South over China's treatment of the Uighurs in Xinjiang.
<br>
<div align="center"><img src='https://Krokke.github.io/Decoding-Biases-in-AI/images/map_pew_all.png' width='100%'></div>  
<div align="center"><u>Net positive impression of China from pew opinion polling, 2019. Values range from -71 in dark orange to 53 in dark blue.</u></div>
<br/><br/>
Interestingly, opinion polling on China is similarly aligned, with the Member States of the EU who have positive impressions of China (Greece, Bulgaria) not counting amongst the condemning countries. It is worth noting that there is a range of public opinion on China among countries that have no official position on the Xinjiang issue.
<br/><br/>
<div align="center"><img src='https://Krokke.github.io/Decoding-Biases-in-AI/images/pew_polling_evolution.png' width='70%'></div>
<div align="center"><u>Evolution of net positive impression of China over time, restricted only to the countries for which there is sufficient data.</u></div>
<br/><br/>
A very limited look at countries for which there is yearly opinion polling on China; positive impressions of the country have been steadily falling since 2017.  (The population size here is only 6 countries.)
<br/><br/>
<div align="center"><img src='https://Krokke.github.io/Decoding-Biases-in-AI/images/map_pol_sel.png' width='100%'></div>  
<div align="center"><u>Geopolitical attitudes towards China's treatment of Uighurs in Xinjiang, 2020. In red, nations that have condemned China; in green, nations that have supported it. The map has been restricted to the group of countries selected for research.</u></div>
<br/><br/>
The geopolitical stance of the countries selected for studying. Among countries with no offical stance, we made an effort to have a variety of public opinion on China, to prevent this category from manifesting some underlying bias.
<br/><br/>
<div align="center"><img src='https://Krokke.github.io/Decoding-Biases-in-AI/images/vid_stance.png' width='60%'></div>  
<div align="center"><u>Histogram of all the video stances in the dataset.</u></div>
<br/><br/>
Looking at the collected search results now, we see a suprisingly large share of pro-china videos on YouTube, at about 30% of all results in the top 20, or roughly half of critical content. This is reflective of Chinese state media's aggressive public relations campaign to push its message on Xinjiang. Balanced content is almost non-existent. Interestingly, the percentage of unrelated content is fairly low, at about 15%. This means that 85% of all content about Xinjiang in the top 20 Youtube search results is related to the allegations of human rights abuse, with other content about Xinjiang in general being mostly sidelined. 
<br/><br/>
<div align="center"><img src='https://Krokke.github.io/Decoding-Biases-in-AI/images/vid_stance_neutral.png' width='60%'></div>  
<div align="center"><u>Histogram of the video stances in the dataset, resticted for the neutral search term 'Xinjiang.</u></div>
<br/><br/>
Even when we look at the same data, but restricting ourselves to the general term 'Xinjiang;, the share of unrelated content only rises to about 20%.
<br/><br/>
<div align="center"><img src='https://Krokke.github.io/Decoding-Biases-in-AI/images/most_freq_vid.png' width='100%'></div>  
<div align="center"><u>A look at the most frequently occuring videos in the dataset.</u></div>
<br/><br/>
Looking at the most frequent search results now, we see that the top two videos are actually pro-China videos created by state media, with the following three being critical content. So while pro-China content remains the minority of search results, some of this content has a high degree of visibility accross YouTube searches. 
<br/><br/>
<div align="center"><img src='https://Krokke.github.io/Decoding-Biases-in-AI/images/model_variables.png' width='60%'></div>  
<div align="center"><u>Categorical data turned into dummified variables for use in statistical modelling.</u></div>
<div align="center"><img src='https://Krokke.github.io/Decoding-Biases-in-AI/images/model_supports.png' width='80%'></div>  
<div align="center"><u>A logistic model predicting a country's geopolitical attitude towards China from the rank-weighted stance of YouTube search results.</u></div>
<div align="center"><img src='https://Krokke.github.io/Decoding-Biases-in-AI/images/model_supports_first_five.png' width='80%'></div>  
<div align="center"><u>The above model run only on the first five results of eeach YouTube search.</u></div>
<div align="center"><img src='https://Krokke.github.io/Decoding-Biases-in-AI/images/most_freq_vid_xinjiang.png' width='80%'></div>  
<div align="center"><u>The most frequently occuring videos in the dataset when searching for the neutral term 'Xinjiang'.</u></div>
<div align="center"><img src='https://Krokke.github.io/Decoding-Biases-in-AI/images/most_freq_vid_xinjiang_terrorism.png' width='90%'></div>  
<div align="center"><u>The most frequently occuring videos in the dataset when searching for the biased term 'Xinjiang Terrorism'.</u></div>
<div align="center"><img src='https://Krokke.github.io/Decoding-Biases-in-AI/images/most_freq_vid_xinjiang_uighurs.png' width='100%'></div>  
<div align="center"><u>The most frequently occuring videos in the dataset when searching for the biased term 'Xinjiang Uighurs'.</u></div>
<div align="center"><img src='https://Krokke.github.io/Decoding-Biases-in-AI/images/model_search_xinjiang_terrorism.png' width='70%'></div>  
<div align="center"><u>An OLS model predicting the rank-weighted stance of a YouTube search result from the search term employed.</u></div>
<div align="center"><img src='https://Krokke.github.io/Decoding-Biases-in-AI/images/model_search_xinjiang_uighurs.png' width='70%'></div>  
<div align="center"><u>The above model run with different variables.</u></div>  

some text 

## Scope

Our experiment underlines the necessity as well as the scope of future research in this area, to deepen our understanding of the algorithms and several variables at play. Firstly, there is an opportunity to study the longitudinal impact by observing the changes in the rankings of videos over a longer period of time, to draw parallels with the evolving geopolitical context in the countries (Hussein et al., 2020). 

Moreover, as the search rankings are influenced by a plethora of factors, namely subscription dynamics, recommendations patterns, optimization strategies etc., and are operating within a larger system, therefore, it presents several possibilities for conducting simultaneous experiments on the confounding variables, in order to enrichen the collective knowledge on the subject (Rieder et al., 2018). 

Additionally, a deeper analysis into the content produced/released in the regional language of respective locations can be utilised for understanding the viewpoint of the masses in the region (Bozdag et al., 2014). Therefore, an inquiry into the YouTube algorithm opens several new frontiers for further research and experimentation, as there is plenty of space to develop understanding of the same. 

Overall as well, there is relatively little knowledge about how the algorithms are impacting geopolitical imaginations, however, the current evidence suggests that increased utilisation of AI algorithms would produce new geopolitical discourses, hence creating more frontiers for further exploration. 

## References

- Bauman, Z., & Lyon, D. (2013). Liquid surveillance: A conversation. John Wiley & Sons.
- Bozdag, E., Gao, Q., Houben, G.-J., & Warnier, M. (2014). Does Offline Political Segregation Affect the Filter Bubble? An Empirical Analysis of Information Diversity for Dutch and Turkish Twitter Users. ArXiv:1406.7438 [Physics]. <https://arxiv.org/abs/1406.7438>
- Bryant, L. V. (2020). The YouTube Algorithm and the Alt-Right Filter Bubble. Open Information Science, 4(1), 85–90. <https://doi.org/10.1515/opis-2020-0007>
- Bucher T (2012) Want to be on the top? Algorithmic power and the threat of invisibility on Facebook. New Media and Society 14(7).
- Edelman BG and Luca M (2014) Digital discrimination: The case of Airbnb.com. Harvard Business School NOM Unit Working Paper No. 14-054. 
- Gillespie T (2014) The relevance of algorithms. In: Gillespie T, Boczkowski P and Foot K (eds) Media Technologies: Essays on Communication, Materiality, and Society. Cambridge, MA: MIT Press.
- Hussein, E., Juneja, P., & Mitra, T. (2020). Measuring Misinformation in Video Search Platforms: An Audit Study on YouTube. Proceedings of the ACM on Human-Computer Interaction, 4(CSCW1), 1–27. <https://doi.org/10.1145/3392854>
- Introna LD and Nissenbaum H (2000) Shaping the Web: Why the politics of search engines matters. The Information Society 16. 
- Kaiser, J., & Rauchfleisch, A. (2020). Birds of a Feather Get Recommended Together: Algorithmic Homophily in YouTube’s Channel Recommendations in the United States and Germany. Social Media + Society, 6(4), 205630512096991. <https://doi.org/10.1177/2056305120969914>
- Ledwich, M., & Zaitsev, A. (2020). Algorithmic extremism: Examining YouTube’s rabbit hole of radicalization. First Monday. <https://doi.org/10.5210/fm.v25i3.10419>
- Machill M, Neuberger C and Schindler F (2003) Transparency on the Net: Functions and deficiencies of Internet search engines. Info 5(1).
- Miailhe, N. (2018). The geopolitics of artificial intelligence: The return of empires? Politique Etrangere, Autumn Issue(3), 105–117. <https://www.cairn-int.info/article-E_PE_183_0105--the-geopolitics-of-artificial.htm>
- Munger, K., & Phillips, J. (2020). Right-Wing YouTube: A Supply and Demand Perspective. The International Journal of Press/Politics, 194016122096476. <https://doi.org/10.1177/1940161220964767>
- Ribeiro, M. H., Ottoni, R., West, R., Almeida, V. A. F., & Meira, W. (2020). Auditing radicalization pathways on YouTube. Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency. <https://doi.org/10.1145/3351095.3372879>
- Rieder, B., Matamoros-Fernández, A., & Coromina, Ò. (2018). From ranking algorithms to “ranking cultures.” Convergence: The International Journal of Research into New Media Technologies, 24(1), 50–68. <https://doi.org/10.1177/1354856517736982>
- Sandvig C, Hamilton K, Karahalios K, et al. (2014) Auditing algorithms: Research methods for detecting discrimination on Internet platforms. In: Data and Discrimination: Converting Critical Concerns into Productive Inquiry, Seattle, USA, 22 May 2014.
- Shifman L (2013) Memes in Digital Culture. Cambridge, MA: MIT Press. 
