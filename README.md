# Forecost
This application uses historical price data for a product to predict when the next best time period would be to buy the product. Uses Microsft Azure Machine Learning Studio with linear regression to predict the time period. Currently there are no plans to make this available onlne. If you would like to check this out, feel free to run it locally. Note, this will only function as long as the machine learning web service is up.

Brought to you by:
[Kent Tsuenchy](https://ca.linkedin.com/in/kent-tsuenchy-0b980159)
[Grady Liu](https://ca.linkedin.com/in/gradyliu)
[Erwang Li](https://ca.linkedin.com/in/erwang-li-a97484126)
[Hamza Khan](https://github.com/hk3212)
[Hussain Punjani](https://github.com/lolzcatz)
[Christopher Zaremba](https://ca.linkedin.com/in/chriszaremba)

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone git@github.com:ktsuench/finhacks-2016.git
$ cd finhacks-2016

$ pip install -r requirements.txt

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).
