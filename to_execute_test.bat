python -m behave --no-capture -f allure_behave.formatter:AllureFormatter -o allureresult\allure features\login\features\test_login.feature & allure serve allureresult\allure