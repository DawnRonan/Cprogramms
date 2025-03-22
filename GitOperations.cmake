# 设置 Git 命令
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
    # 执行 git add 和 commit
    # 输出调试信息
    message(STATUS "Running Git status check...")
    execute_process(COMMAND ${GIT_ADD_COMMAND} WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
    execute_process(COMMAND ${GIT_COMMIT_COMMAND} WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})

endif()
