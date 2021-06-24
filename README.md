# Twitter-Data-Analysis


### Folder Structure
    clean_tweets_dataframe-contains the program for cleaning the dataframe retrieved from the twitter data through extract dataframe
    extract_dataframe-contains code for extracting the dataframe from the json file
    .travis.yml- contains configuration for travis CI
    requirements.txt-contains required libraries for running scripts
    data-folder containing data files
        covid19.json-contains the twitter data in a json format
    test-folder containing test
        test_clean_daragram-contains test cases to test cleaning the dataframe
        test_extract_dataframe-contains test cases to test the extraction of the dataframe


### So here are the bare minimum requirement for completing this task

1. Fork repository to your github account
2. Create a branch called “fix_bug” to fix the bugs in the fix_clean_tweets_dataframe.py and fix_extract_dataframe.py 
3. In branch `fix_bug` copy or rename `fix_clean_tweets_dataframe.py` to `clean_tweets_dataframe.py` and `fix_extract_dataframe.py`  to `extract_dataframe.py` 
4. Fix the bugs on `clean_tweets_dataframe.py` and `extract_dataframe.py` 
5. Multiple times push the code you are working on to git, and once the fix is complete, merge the `fix_bug` branch to master
6. Create a new branch called `make_unittest` for creating a new unit test for extract_dataframe.py code.
7. After completing the unit test writing, merge  “make_unittest”  to main branch
8. In all cases when you merge, make sure you first do Pull Request, review, then accept the merge.
9. Setup Travis CI to your repository such that when you git push new code (or merge a branch) to the main branch, the unit test in tests/*.py runs automatically. 10. All tests should pass.

After Completing this Challenge, you would have explore  

- Unittesting
- Modular Coding
- Software Engineering Best Practices
- Python Package Structure
- Bug Fix (Debugging)

Have Fun and Cheers
