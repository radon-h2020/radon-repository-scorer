![Build](https://github.com/radon-h2020/radon-repository-scorer/workflows/Build/badge.svg)
![lgtm](https://img.shields.io/lgtm/grade/python/github/radon-h2020/radon-repository-scorer)
![pypi-version](https://img.shields.io/pypi/v/repository-scorer)
![pypi-status](https://img.shields.io/pypi/status/repository-scorer)
![release-date](https://img.shields.io/github/release-date/radon-h2020/radon-repository-scorer)
![python-version](https://img.shields.io/pypi/pyversions/repository-scorer)

# radon-repository-scorer
The radon-repository-scorer is a Python package to compute a repository best engineering practices indicators.

The module provides the following 8 indicators of well-engineered software projects:

* **Core contributors:** the number of contributors whose total number of commits accounts for 80% or more of the total contributions.
* **Continuous integration (CI):** the repository has evidence of a CI service, determined by the presence of a configuration file required by that service (e.g., a.travis.ymlfor TravisCI).
* **Comments ratio:** ratio between comments and lines of code.
* **Commit frequency:** the average number of commits per month.
* **Issue frequency:** the average number of issue events transpired per month.
* **License availability:** the repository has evidence of a license (i.e., a LICENSE file).
* **Lines of Code:** the number of executable lines of code. 
* **Ratio of IaC scripts:** ratio between Infrastructure-as-Code (IaC) files and total files.


All the previous indicators but the last are described in depth in:

```text
@inproceedings{@article{munaiah2017curating,
  title={Curating GitHub for engineered software projects},
  author={Munaiah, Nuthan and Kroh, Steven and Cabrey, Craig and Nagappan, Meiyappan},
  journal={Empirical Software Engineering},
  volume={22},
  number={6},
  pages={3219--3253},
  year={2017},
  publisher={Springer}
}
```
          

**Note:** the tool is intended to be used as a Python library. 
Therefore, the current version does not provide a command line interface.

## How to install

**From the Python Package Index** 

```pip install repository-scorer```

<br>

**From source code**
```
pip install -r requirements
pip install .
```


## How to use

```python
from reposcorer.scorer import score_repository

report = score_repository(path_to_repo='path/to/cloned/repo',
                          full_name_or_id='repo_owner/repo_name',  # e.g., radon-h2020/radon-repository-scorer
                          host='github',  # or gitlab
                          calculate_comments_ratio= True,
                          calculate_commit_frequency=True,
                          calculate_core_contributors=True,
                          calculate_has_ci=True,
                          calculate_has_license=True,
                          calculate_iac_ratio=True,
                          calculate_issue_frequency=True,
                          calculate_repository_size=True)
```

**Output**
```text
{
  'has_ci': <bool>,
  'comments_ratio': <float in [0,1]>,
  'commit_frequency': <float>,
  'core_contributors': <int>,
  'iac_ratio': <float in [0,1]>,
  'issue_frequency': <float>,
  'has_license': <bool>,
  'repository_size': <int>
}
``` 


See [CHANGELOG](CHANGELOG.md) for logs detail about releases.
