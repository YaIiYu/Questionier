import os
import json

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "questions.json"
path = os.path.join(script_dir, rel_path)

def write_json(data, filename=path):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()

def get_question(question_id):
    result = None
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        temp = data["questions"]
        for user in temp:
            # print('user')
            if user['id'] == question_id:
                result = user
                # print(user['username'] == username)

    return result

def get_test(test_id):
    result = None
    rel_path_1 = "tests.json"
    path_1 = os.path.join(script_dir, rel_path_1)
    with open(path_1, 'r', encoding='utf-8') as f:
        data = json.load(f)
        temp = data["tests"]
        for test in temp:
            if test['title'] == test_id:
                result = test
                break
    return result

def get_test_by_id(test_id):
    result = None
    rel_path_1 = "tests.json"
    path_1 = os.path.join(script_dir, rel_path_1)
    with open(path_1, 'r', encoding='utf-8') as f:
        data = json.load(f)
        temp = data["tests"]
        for test in temp:
            #print(f"test_id: {test['id']}")
            if test['id'] == test_id:
                result = test
                break
    return result
                # print(user['username'] == username)


def get_all_tests():
    result = []
    rel_path_1 = "tests.json"
    path_1 = os.path.join(script_dir, rel_path_1)
    with open(path_1, 'r', encoding='utf-8') as f:
        data = json.load(f)
        temp = data["tests"]
        for user in temp:
            result.append(user)

        return result

def user_reg(user_id, test_id):
    # print(path)
    cond = is_passing_test_now(user_id)
    print(cond)
    if cond is False:
        rel_path_1 = "user_answers.json"
        path_1 = os.path.join(script_dir, rel_path_1)
        with open(path_1, 'r') as f:
            data = json.load(f)
            temp = data["users"]
            mom = {"id": user_id, "test_id": test_id, "question_answered": 0, "question_answers": [], "is_done": False}
            temp.append(mom)
            f.close()
        write_json(data, path_1)


def get_user(user_id):
    result = None
    rel_path_1 = "user_answers.json"
    path_1 = os.path.join(script_dir, rel_path_1)
    with open(path_1, 'r', encoding='utf-8') as f:
        data = json.load(f)
        temp = data["users"]
        for user in temp:
            if user["id"] == user_id and user['is_done'] != True:
                result = user
                break

        return result

def is_passing_test_now(user_id):
    result = False
    rel_path_1 = "user_answers.json"
    path_1 = os.path.join(script_dir, rel_path_1)
    with open(path_1, 'r', encoding='utf-8') as f:
        data = json.load(f)
        temp = data["users"]

        for user in temp:
            if user["id"] == user_id:
                if user["is_done"] is False:
                    result = True
                    break
        return result

def update_user_value(user_id, string_name, value):
    rel_path_1 = "user_answers.json"
    path_1 = os.path.join(script_dir, rel_path_1)
    with open(path_1, 'r') as f:
        data = json.load(f)
        temp = data["users"]
        for user in temp:
            if user["id"] == user_id and user['is_done'] != True:
                user[f"{string_name}"] = value
        # print(user['username'] == username)
        f.close()

    with open(path_1, "w") as f:
        json.dump(data, f, indent=4)
        f.close()




