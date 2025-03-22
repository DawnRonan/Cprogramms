cmake_minimum_required(VERSION 3.10)

project(CPrograms)

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 11)


# 设置 Git 操作的自动化命令
include(${CMAKE_SOURCE_DIR}/GitOperations.cmake)


# 自动提交 Git
add_custom_target(git_commit
    COMMAND ${CMAKE_COMMAND} -P ${CMAKE_SOURCE_DIR}/GitOperations.cmake
    COMMENT "Running Git operations"
)
