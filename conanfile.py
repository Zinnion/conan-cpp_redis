from conans import ConanFile, CMake, tools


class CppredisConan(ConanFile):
    name = "cpp_redis"
    version = "5.0.0"
    license = "The MIT License (MIT)"
    url = "https://github.com/zinnion/conan-cpp_redis"
    description = "Conan recipe for Cpp_Redis"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone --recurse-submodules https://github.com/cpp-redis/cpp_redis.git")
        self.run("cd cpp_redis && git checkout master")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("cpp_redis/CMakeLists.txt", "project(${PROJECT} CXX)",
                              '''project(${PROJECT} CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="cpp_redis")
        cmake.build()

    def package(self):
        self.copy("*", dst="include", src="cpp_redis/includes")
        self.copy("*.hpp", dst="include", src="cpp_redis/includes")
        self.copy("*.ipp", dst="include", src="cpp_redis/includes")
        self.copy("*", dst="include", src="cpp_redis/tacopie/includes")
        self.copy("*.hpp", dst="include", src="cpp_redis/tacopie/includes")
        self.copy("*cpp_redis.lib", dst="lib", keep_path=False)
        self.copy("*tacopie.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["cpp_redis","tacopie"]

