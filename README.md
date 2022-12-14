# Recommender Systems

# Objectives:

- [x] Learn about the different types of recommendation systems
- [x] Review and collect courses and information about the topic 
- [x] Explore the *content based* and *collaborative filter* recommenders using the movielens dataset
- [x] Evaluate the performance of the above recommenders in predicting user preferences using some metrics
- [ ] Compare the CO2 footprint of each of the above recommender system
- [ ] Build a hybrid system of the above systems
- [ ] Build an End to End recommendation system (in the cloud)
- [ ] Build a small App (using Django or fastapi) with the recommendation system

# Files

The work includes the following notebooks

- [x] [recommender_systems_overview.ipynb](https://github.com/morschulik/recommender-system/blob/V3/Notebooks/recommender_systems_overview.ipynb) 
- [x] [RS_workflow_in_cloud.ipynb](https://github.com/morschulik/recommender-system/blob/V3/Notebooks/RS_workflow_in_cloud.ipynb) 
- [x] [CB_Recommender_movielens.ipynb](https://github.com/morschulik/recommender-system/blob/V3/Notebooks/CB_Recommender_movielens.ipynb)
- [x] [CF_Recommender_movielens.ipynb](https://github.com/morschulik/recommender-system/blob/V3/Notebooks/CF_Recommender_movielens.ipynb)
- [ ] [CB_vs_CF_Evaluation.ipynb](https://github.com/morschulik/recommender-system/blob/V3/Notebooks/CB_vs_CF_Evaluation.ipynb)
- [ ] [CO2_footprint_CB_vs_CF.ipynb](https://github.com/morschulik/recommender-system/blob/V3/Notebooks/CO2_footprint_CB_vs_CF.ipynb)
- [x] [outlook_and_further_work.ipynb](https://github.com/morschulik/recommender-system/blob/V3/Notebooks/outlook_and_further_work.ipynb) 
- [x] [Dataset_description.ipynb](https://github.com/morschulik/recommender-system/blob/V3/Notebooks/Dataset_description.ipynb)


# References

"...the **go to** statement should be abolished..." [[1]](#1).<br>

Many of the pictures of the overview are screenshots of the references below:


#### Sources for an overview to recommender systems:
<a id="1">[1]</a> [Google cloud skill boost course](https://www.cloudskillsboost.google/course_templates/39) <br>
<a id="2">[2]</a> [Also the Gliederung here: Recommendation systems with tensorflow](https://www.pluralsight.com/courses/recommendation-systems-tensorflow-google-cloud) <br>
<a id="3">[3]</a> [A GitHub Repository about building a recommender system with Tensorflow](https://github.com/GoogleCloudPlatform/tensorflow-recommendation-wals/blob/master/notebooks/Part1.ipynb) <br>
From the above notebook we can find a way to get and download the data in the notebook <br>
<a id="4">[4]</a> [Google Developer course](https://developers.google.com/machine-learning/recommendation/overview) <br>
<a id="5">[5]</a> [Singapore group talk ](https://www.youtube.com/watch?v=5Lm1UMogEkI) <br>
<a id="6">[6]</a> [GitHub Repo of the Singapore group](https://github.com/karthikmswamy/RecSys/blob/master/Train_RecSys.ipynb) <br>
<a id="7">[7]</a> [Phases of recommendation process](https://www.sciencedirect.com/science/article/pii/S1110866515000341)<br>

#### Sources for Content bases, collaborative filtering and deap learning using Movielense Dataset
<a id="8">[8]</a> [Content based Recommender](https://medium.com/analytics-vidhya/content-based-recommender-systems-in-python-2b330e01eb80)<br>
<a id="9">[9]</a> [Movielens - Content Based](https://www.kaggle.com/code/indralin/movielens-project-1-1-content-based)<br>
<a id="10">[10]</a> [Movielens - Collaborative Filtering](https://www.kaggle.com/code/indralin/movielens-project-1-2-collaborative-filtering)<br>
<a id="11">[11]</a> [Movielense - Deep Learning](https://www.kaggle.com/code/indralin/movielens-project-1-3-deep-learning)<br>
<a id="12">[12]</a> [Movielense Github Project- Different Recommenders](https://github.com/rposhala/Recommender-System-on-MovieLens-dataset/blob/main/README.md)<br>


##### Sources about other recommendation types
<a id="13">[13]</a> [Another project with good explanation of the deep learning recommender model is here](https://blog.codecentric.de/bigquery-ml-schnelles-training-recommendation-modell)<br>
<a id="14">[14]</a> [And here (matrix factorization)](https://medium.com/google-cloud/recommendation-systems-with-deep-learning-69e5c1772571) <br>
<a id="15">[15]</a> [What are Recommendation systems Machine learning](https://www.analyticssteps.com/blogs/what-are-recommendation-systems-machine-learning)

#### Sources about the Evaluation of the Recommending Algorithms
<a id="16">[16]</a> [Monitor your models in production - Evaluation metrics](https://neptune.ai/blog/how-to-monitor-your-models-in-production-guide)<br>
<a id="17">[17]</a> [Evaluation metrics of recommender Systems](https://neptune.ai/blog/recommender-systems-metrics )<br>

##### Sources for comparing content base vs collaborative filtering
<a id="18">[18]</a> [CF and CF differences and similarities](https://arxiv.org/pdf/1912.08932.pdf) <br>
<a id="19">[19]</a> [CF vs CF](https://analyticsindiamag.com/collaborative-filtering-vs-content-based-filtering-for-recommender-systems/) <br>
<a id="20">[20]</a> [Performance metrics CB vs CF](https://medium.com/analytics-vidhya/movie-recommender-system-using-content-based-and-collaborative-filtering-84a98b9bd98e)<br>

#### Sources for the Outlook - Building an End to End Recommendation system (in the cloud)
<a id="21">[21]</a> [Building a recommender system in the cloud(GCP)](https://cloud.google.com/recommender/docs/key-concepts?hl=en) <br>
<a id="22">[22]</a> [workflow of building a recommendation system in the cloud:(Azure)](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/ai/movie-recommendations-with-machine-learning)<br>
<a id="23">[23]</a> [7 Steps to build/design a recommendation systems - Build a content based recommender in the cloud](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/build-content-based-recommendation-system-using-recommender)<br>
<a id="24">[24]</a> [Feature Engineering/Preprocessing 1 - One of the steps to build a recommendation system(Azure)](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-auto-features#feature-engineering-and-featurization)<br>
<a id="25">[25]</a> [Feature Engineering/Preprocessing 2 - One of the steps to build a recommendation system(GCP)](https://cloud.google.com/architecture/data-preprocessing-for-ml-with-tf-transform-pt1)<br>
<a id="26">[26]</a> [Deploying the models - One of the steps of building a recommendation system in the cloud](https://cloud.google.com/ai-platform/prediction/docs/deploying-models)<br>

