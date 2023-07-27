import requests

def get_todo_list_progress(employee_id):
    url = "https://api.example.com/todo/list/progress"
    params = {"employee_id": employee_id}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception("Error getting TODO list progress")

    data = response.json()
    name = data["name"]
    done_tasks = data["done_tasks"]
    total_tasks = data["total_tasks"]

    print(f"Employee {name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in data["completed_tasks"]:
        print("\t" + task)

if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    get_todo_list_progress(employee_id)

