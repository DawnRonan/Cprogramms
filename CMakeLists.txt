cmake_minimum_required(VERSION 3.10)

project(CPROGRAMS)

# 设置Git命令
set(GIT_ADD_COMMAND "git add .")
set(GIT_COMMIT_COMMAND "git commit -m \"Auto commit by CMake\"")

# 检查是否有文件更改
execute_process(
    COMMAND git status --porcelain
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    RESULT_VARIABLE GIT_STATUS_RESULT
    OUTPUT_VARIABLE GIT_STATUS_OUTPUT
    ERROR_QUIET
)

if (NOT GIT_STATUS_RESULT EQUAL 0)
    message("No changes to commit.")
else()
    # 执行git add 和 commit
    execute_process(COMMAND git add . WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
    execute_process(COMMAND git commit -m "Auto commit by CMake" WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()

