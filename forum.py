{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_zlHuu6FK-qH"
      },
      "outputs": [],
      "source": [
        "#_____________________________________________________________________________\n",
        "class User:\n",
        "\n",
        "  login_attempts = 0\n",
        "\n",
        "  def __init__(self, first_name, last_name, password, nickname, age, sex, karma):\n",
        "    self.first_name = first_name\n",
        "    self.last_name = last_name\n",
        "    self.password = password\n",
        "    self.nickname = nickname\n",
        "    self.age = age\n",
        "    self.sex = sex\n",
        "    self.karma = karma\n",
        "\n",
        "  def increment_login_attempts(self):\n",
        "    self.login_attempts += 1\n",
        "    print(f'Login attempt...\\nTotal login attempts: {self.login_attempts}')\n",
        "\n",
        "  def reset_login_attempts(self):\n",
        "    self.login_attempts = 0\n",
        "    print(f'Login attempts reset...\\nNumber of login attempts is now: {self.login_attempts}')\n",
        "\n",
        "  def describe_user(self):\n",
        "    print(f'This is {self.first_name} {self.last_name}')\n",
        "    print(f'Nickname: {self.nickname}')\n",
        "    print(f'Password: {self.password}')\n",
        "    print(f'Age: {self.age}')\n",
        "    print(f'Sex: {self.sex}')\n",
        "    print(f'Current karma: {self.karma}\\n')\n",
        "\n",
        "  def greet_user(self):\n",
        "    print(f'Greetings, {self.nickname}! How do you do? ;)\\n')\n",
        "\n",
        "jerry = User('Jerry', 'Statham', 'TdcdcI', 'Jerry777', 43, 'Male', 632)\n",
        "david = User('David', 'Dother', 'n4OtzR', 'SaintServ', 24, 'Male', 151)\n",
        "joey = User('Joseph', 'Tribbiani', 'ZL7Nd6', 'Joey', 32, 'Male', 69)\n",
        "#_____________________________________________________________________________\n",
        "class Privileges:\n",
        "\n",
        "  def __init__(self, privileges = ['allowed to add posts', 'allowed to delete users', 'allowed to ban users']):\n",
        "    self.privileges = privileges\n",
        "\n",
        "  def show_privileges(self):\n",
        "    print('Privileges:')\n",
        "    for item in self.privileges:\n",
        "      print(item)\n",
        "#_____________________________________________________________________________\n",
        "class Admin(User):\n",
        "\n",
        "  def __init__(self, first_name, last_name, password, nickname, age, sex, karma):\n",
        "    super().__init__(first_name, last_name, password, nickname, age, sex, karma)\n",
        "    self.privileges = Privileges()\n",
        "\n",
        "rachel = Admin('Rachel', 'Green', 'axoNcE', 'Rachy', 34, 'Female', 1000)"
      ]
    }
  ]
}
