# Location Bias in Youtube's Search Engine
*Does the Youtube search ranking algorithm reflect national geopolitics?*

- [Introduction](#introduction)
- [Literature review and approach](#literature-review-and-approach)
- [Methodology](#methodology)
- [Results](#results)
- [Project scope](#scope)

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

<head>
    <style>
        body {
            text-align: center;
	}
    </style>
</head>

<figure>
	<img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/map_pol_all.png' width='100%'>
	<figcaption>GeeksforGeeks Logo</figcaption>
</figure>

<figure>
<img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/map_pol_sel.png' width='100%'>
	<figcaption>GeeksforGeeks Logo</figcaption>
</figure>

<figure>
<img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/map_pew_all.png' width='100%'>
	<figcaption>GeeksforGeeks Logo</figcaption>
</figure>

<figure>
<img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/map_pew_sel.png' width='100%'>
	<figcaption>GeeksforGeeks Logo</figcaption>
</figure>

<div class="container">
    <div style="float:left">
	    <img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/vid_stance.png' width='50%'>
    </div>
    <div style="float:right">
	    <img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/vid_stance_neutral.png' width='50%'>
    </div>
</div>
<img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/pew_polling_evolution.png' width='70%'>
<img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/most_freq_vid.png' width='70%'>
<img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/model_variables.png' width='70%'>
<img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/model_supports.png' width='70%'>
<img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/model_supports_first_five.png' width='70%'>
<img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/most_freq_vid_xinjiang.png' width='70%'>
<img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/most_freq_vid_xinjiang_terrorism.png' width='70%'>
<img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/most_freq_vid_xinjiang_uighurs.png' width='70%'>
<img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/model_search_xinjiang_terrorism.png' width='70%'>
<img src='https://Krokke.github.io/Decoding-Biases-in-AI/Images/model_search_xinjiang_uighurs.png' width='70%'>

## Scope
