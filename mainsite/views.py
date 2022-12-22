from django.shortcuts import render
import random
import subprocess
import sys
import os

# Create your views here.


def home(request):
    language = 'Select language'
    data = {
        'language': language,
    }
    return render(request, "mainsite/home.html", data)


def runcode(request):
    if request.method == 'POST':
        lang_select = request.POST['language']
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n", " ").split(" ")


        def input():
            a = input_part[0]
            del input_part[0]
            return a


        if(lang_select == 'c'):
                f = open("main.c", 'w')
                f.write(code_part)
                f.close()
                data, temp = os.pipe()

                os.write(temp, bytes(y, "utf-8"))
                os.close(temp)
                try:
                    s = subprocess.check_output(
                        "gcc main.c -o out1;./out1", stdin=data, shell=True,stderr=subprocess.STDOUT)

                except subprocess.CalledProcessError as e:
                    raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

                # s = subprocess.check_output(
                #     "gcc main.c -o out1;./out1", stdin=data, shell=True)
                output = s.decode("utf-8")

                data = {
                    # "language": lang_select,
                    "code": code_part,
                    "input": y,
                    "output": output,
                }

        elif(lang_select == 'python'):
            try:
                orig_stdout = sys.stdout
                sys.stdout = open('file.txt', 'w')
                exec(code_part)
                sys.stdout.close()
                sys.stdout = orig_stdout
                output = open('file.txt', 'r').read()
            except Exception as e:
                sys.stdout.close()
                sys.stdout = orig_stdout
                output = e
                print(output)

            data = {
                # "language": lang_select,
                "code":code_part,
                "input": y,
                "output": output
            }

        elif(lang_select == 'c++'):
            f = open("try.cpp", 'w')
            f.write(code_part)
            f.close()
            data, temp = os.pipe()
            os.write(temp, bytes(y, "utf-8"));
            os.close(temp)
            try:
                s = subprocess.check_output(
                    "g++ try.cpp -o out2;./out2", stdin=data, shell=True,stderr=subprocess.STDOUT)

            except subprocess.CalledProcessError as e:
                raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

            # s = subprocess.check_output("g++ try.cpp -o out2;./out2", stdin = data, shell = True)
            output = s.decode("utf-8")
            data = {
                # "language": lang_select,
                "code":code_part,
                "input": y,
                "output": output
            }

    res = render(request, 'mainsite/home.html', data)
    return res
