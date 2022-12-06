# recommender-systems

# ToDo edit the draft of this readme 


#### Objectives: #todo

- review and collect courses and Infomrations about the topic
- Explore the conent based and collaborative filter recommender on movielens dataset
- Build an End to End recommendation system


#### Dataset description

#todo write the features from here or from the screenshots https://www.tensorflow.org/datasets/catalog/movielens

#ToDo :edit the acknowledgment of the dataset

@article{10.1145/2827872,
author = {Harper, F. Maxwell and Konstan, Joseph A.},
title = {The MovieLens Datasets: History and Context},
year = {2015},
issue_date = {January 2016},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {5},
number = {4},
issn = {2160-6455},
url = {https://doi.org/10.1145/2827872},
doi = {10.1145/2827872},
journal = {ACM Trans. Interact. Intell. Syst.},
month = dec,
articleno = {19},
numpages = {19},
keywords = {Datasets, recommendations, ratings, MovieLens}
}



# todo Data can be downloaded from https://grouplens.org/datasets/movielens/20m/

#todo similar to [here](https://github.com/GoogleCloudPlatform/tensorflow-recommendation-wals/blob/master/notebooks/Part1.ipynb) 

# to do The MovieLens data set
edit the following to replace the 100k by the 20 m dataset

Execute the following cell to download the MovieLens 100k data set:

```
!curl -O 'http://files.grouplens.org/datasets/movielens/ml-100k.zip'
!unzip ml-100k.zip
!mkdir -p ../data
!cp ml-100k/u.data ../data/
```


     



#### Files

The work would includes the following notebooks

- recommender_systems_overview.ipynb ---> includes the phases of building a recommendation system and  a basic overview of the filtering systems (with pictures from the google cloud course)
- RS_workflow_in_cloud.ipynb ---> Pictures of the workflow from AWS, GCP, Azure
- CB_Recommender_movielens.ipynb
- FB_Recommender_movielens.ipynb

- CB_vs_FB_Evaluation.ipynb
- CO2_foot_print_CB_vs_FB.ipynb

- outlook_and_further_work.ipynb (or as subsection here) (includes building end to end recommendation system)



#### sources # todo check how to make the sources well and edit the following section

Many of the pictures of the overview are screenshots of the references below:
[1](https://www.cloudskillsboost.google/course_templates/39)
[2](https://www.youtube.com/watch?v=5Lm1UMogEkI)

[](https://github.com/karthikmswamy/RecSys/blob/master/Train_RecSys.ipynb)

[](https://developers.google.com/machine-learning/recommendation/overview)

[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()

https://neptune.ai/blog/how-to-monitor-your-models-in-production-guide <br>

# todo further sources  (needs to be edited)
https://neptune.ai/blog/recommender-systems-metrics (mean , rmsqs, map, etc)

workflow in the cloud providers:(z.B Azur) (these are general steps then go to the feetures of the movielens describing its featuresfrom tensorflow)

https://learn.microsoft.com/en-us/azure/architecture/example-scenario/ai/movie-recommendations-with-machine-learning

Workflow of the content based re commender (get the picture from there)

https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/build-content-based-recommendation-system-using-recommender

steps to build/design the recommendation system:
1……..8?
one of those steps is called https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-auto-features#feature-engineering-and-featurization

Phases of recommendation process(https://www.sciencedirect.com/science/article/pii/S1110866515000341)


##### sources for comparing content base vs colborative filtering
https://arxiv.org/pdf/1912.08932.pdf

https://analyticsindiamag.com/collaborative-filtering-vs-content-based-filtering-for-recommender-systems/

comparing the data:

https://medium.com/analytics-vidhya/movie-recommender-system-using-content-based-and-collaborative-filtering-84a98b9bd98e


### sourses for outlook further works:
a project that used the tensorflow to build a recommender system is available here
https://github.com/GoogleCloudPlatform/tensorflow-recommendation-wals/blob/master/notebooks/Part1.ipynb
from the above notebook we can find a way to get and download the data in the notebook

also the gliederung here:
https://www.pluralsight.com/courses/recommendation-systems-tensorflow-google-cloud


another project with good explanaation of the third model is here
https://blog.codecentric.de/bigquery-ml-schnelles-training-recommendation-modell

and here : https://medium.com/google-cloud/recommendation-systems-with-deep-learning-69e5c1772571
(matrix factorization)

https://www.analyticssteps.com/blogs/what-are-recommendation-systems-machine-learning

(Using tensorflow , add summery of the concepttraining data, vs tet data )

group from singapore
https://www.youtube.com/watch?v=5Lm1UMogEkI
their repo
https://github.com/karthikmswamy/RecSys/blob/master/Train_RecSys.ipynb


google developer:
https://developers.google.com/machine-learning/recommendation

Google cloud is offering solutions for recommendation system, thay were offering tuotrial on how to use tesorflow to build machine learning but they are unavailable now

new links :
https://cloud.google.com/recommender/docs/key-concepts?hl=en
https://cloud.google.com/architecture/data-preprocessing-for-ml-with-tf-transform-pt1
https://cloud.google.com/ai-platform/prediction/docs/deploying-models

old links (not available or redirect to the cloud artichecture center)
https://cloud.google.com/solutions/machine-learning/recommendation-system-tensorflow-overview
https://cloud.google.com/solutions/machine-learning/recommendation-system-tensorflow-deploy


