def aws_iam_check_if_policy_exist(iam):
    try:
        # Get a policy
        response = iam.get_policy(
            PolicyArn='arn:aws:iam::791797855262:policy/service-role/AWSAthenaSparkRolePolicy-3qkpg41t'
        )
        print(response['Policy'])
    except Exception as e:
        print("error occured while invoking aws_iam_check_if_policy_exist and error is {}".format(e))
        return False
    else:
        return True


def aws_iam_check_if_role_exist(iam):
    try:
        # Get a policy
        response = iam.get_role(
            RoleName='github-oidc-role'
        )
        print(response['Role'])
    except Exception as e:
        print("error occured while aws_iam_check_if_role_exist and error is {}".format(e))
        return False
    else:
        return True
