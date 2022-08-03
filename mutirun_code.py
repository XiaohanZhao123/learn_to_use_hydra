import os

if __name__ == '__main__':
    classfication_list = ['logistic','svm']
    regression_list = ['lasso','ls']
    run_code = "classification=" + ','.join(classfication_list) + '  regression=' + ','.join(regression_list)
    python_env = 'C:/Conda/python.exe'
    python_script = 'multirun.py --multirun'
    code = '  '.join((python_env,python_script,run_code))
    os.system(code)
