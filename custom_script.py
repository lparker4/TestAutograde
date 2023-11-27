import subprocess
import os
import shutil
import subprocess
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from threading import Thread, ThreadError



# Code for running the cells independently of the autograde library
from json import load

directory = 'sci10_submissions'
test_script_name = "sci10_test.py"
results_dir_name = "results"
context_dir_name = "context"
# directory = 'recursion_assignments'
# test_script_name = "recursion_test.py"
# results_dir_name = "recursion_results"
# directory = 'turtle_colabs'
# test_script_name = "turtle_test.py"
# results_dir_name = "turtle_results"

new_files_dir = "artifacts"

main_dir = os.getcwd()
artifacts_dir = os.path.join(main_dir, new_files_dir)

assignments_dir = os.path.join(main_dir, directory)
assignments_dir = os.path.join(main_dir, directory)
original_files = os.listdir(main_dir)
assignments_dir = os.path.join(main_dir, directory)
for file in os.listdir(assignments_dir):
    path = os.path.join(assignments_dir, file)
    print(path)
    if os.path.isfile(path):
        shutil.copy(path, main_dir)

        args = ["autograde", "test", test_script_name, file, "--target", results_dir_name, "--context", context_dir_name]
        subprocess.Popen(args)
    else:
        print("DID NOT RUN")
        
# for file in os.listdir(assignments_dir):
#     path = os.path.join(assignments_dir, file)
#     print(path)
#     if os.path.isfile(path):
#         shutil.copy(path, main_dir)
    
#     with open(file, encoding="utf8") as fp:
#         nb = load(fp)
#     cell_count = 0 # for debugging

#     for cell in nb['cells']:
        
#         if cell['cell_type'] == 'code':

#             source = ''.join(line for line in cell['source'] if not line.startswith('%'))

#             try:
#                 exec(source, globals(), locals())
#             except Exception as exc:
#                 print("Cell {} did not run correctly in {}\nError message:\n{}".format(cell_count, file, exc))
#         # See if any new files have been added, move them to another results folder, and delete them.
#         current_files = os.listdir(main_dir)
#         unique_files =  set(current_files).difference(set(original_files).difference(set([os.path.join(main_dir, file)])))


#         for new_file in unique_files:
#             if new_file.split(sep=".")[1] != "ipynb":
#                 path = os.path.join(main_dir, new_file)
#                 shutil.copy(path, artifacts_dir)
#                 new_name = "{}_{}.{}".format(file.split(sep=".")[0], cell_count, new_file.split(sep=".")[1])
#                 os.rename(os.path.join(artifacts_dir, new_file), os.path.join(artifacts_dir, new_name))
#                 os.remove(os.path.join(main_dir, new_file))
            
#         cell_count += 1
    


# Turtle code trial

# def execute_python_file(file_path):
#    try:
#       completed_process = subprocess.run(['python', file_path], capture_output=True, text=True)
#       if completed_process.returncode == 0:
#          print("Execution successful.")
#          print("Output:")
#          print(completed_process.stdout)
#       else:
#          print(f"Error: Failed to execute '{file_path}'.")
#          print("Error output:")
#          print(completed_process.stderr)
#    except FileNotFoundError:
#       print(f"Error: The file '{file_path}' does not exist.")

# def run_nbs(assignments_dir):
#     for file in os.listdir(assignments_dir):
#         # text = "jupyter nbconvert --to python {}".format(file)
#         # exec(text, globals(), locals())
#     #     args = ["jupyter", "nbconvert", "--to", "python",file]
#     #     subprocess.Popen(args)
#     # for file in os.listdir(assignments_dir):
#     #     if file.split(sep=".")[1] == "py":
#     #         execute_python_file(file)

#         print("Now starting process for: file")
#         with open(file) as ff:
#             nb_in = nbformat.read(ff, nbformat.NO_CONVERT)
            
#         ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
#         # output of all cells in a notebook format
#         nb_out = ep.preprocess(nb_in)
    

    

# def check_artifacts(main_dir, artifacts_dir):
#         # See if any new files have been added, move them to another results folder, and delete them.
#     original_files = os.listdir(main_dir)
#     img_count = 0

#     while(1):
#         current_files = os.listdir(main_dir)
#         unique_files =  set(current_files).difference(set(original_files).difference(set([os.path.join(main_dir, file)])))

#         for new_file in unique_files :
#             print(new_file)
#             path = os.path.join(main_dir, new_file)
#             shutil.copy(path, artifacts_dir)
#             new_name = "{}_{}.{}".format(file.split(sep=".")[0], img_count, new_file.split(sep=".")[1])
#             os.rename(os.path.join(artifacts_dir, new_file), os.path.join(artifacts_dir, new_name))
#             os.remove(os.path.join(main_dir, new_file))
#             img_count += 1

# if __name__ =="__main__":
#     # directory = 'recursion_assignments'
#     # test_script_name = "recursion_test.py"
#     # results_dir_name = "recursion_results"
#     # directory = 'turtle_colabs'
#     # test_script_name = "turtle_test.py"
#     # results_dir_name = "turtle_results"
#     directory = 'sci10_submissions'
#     test_script_name = "sci10_test.py"
#     results_dir_name = "results"

#     new_files_dir = "artifacts"

#     main_dir = os.getcwd()
#     artifacts_dir = os.path.join(main_dir, new_files_dir)
    
#     assignments_dir = os.path.join(main_dir, directory)
#     for file in os.listdir(assignments_dir):
#         path = os.path.join(assignments_dir, file)
#         print(path)
#         if os.path.isfile(path):
#             shutil.copy(path, main_dir)

#             args = ["autograde", "test", test_script_name, file, "--target", results_dir_name]
#             subprocess.Popen(args)
#             # os.remove(os.path.join(main_dir, file))

#     t_run_nbs = Thread(target=run_nbs, daemon=True, args=[assignments_dir])
#     t_artifacts = Thread(target=check_artifacts, args=[main_dir, artifacts_dir])
#     t_run_nbs.start()

#     t_artifacts.start()
