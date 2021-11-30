GEN ?= cmake
BUILD_TYPE ?= Debug
BUILD_DIR=$(CURDIR)/_build/$(GEN)/$(BUILD_TYPE)
INSTL_DIR=$(CURDIR)/_install/$(GEN)/$(BUILD_TYPE)

all: cmake_coverage

CMAKE_OPTIONS = -H$(CURDIR)
CMAKE_OPTIONS += -B$(BUILD_DIR)
CMAKE_OPTIONS += -DCMAKE_INSTALL_PREFIX=$(INSTL_DIR)

ifeq ($(GEN), xcode)
	CMAKE_OPTIONS += -G "Xcode"
else
	CMAKE_OPTIONS += -G "Unix Makefiles"
endif

ifeq ($(BUILD_TYPE), Debug)
	CMAKE_OPTIONS += -DCMAKE_VERBOSE_MAKEFILE=ON
	CMAKE_OPTIONS += -DCMAKE_BUILD_TYPE=Debug
else
	CMAKE_OPTIONS += -DCMAKE_BUILD_TYPE=Release
endif

cmake_config:
	cmake $(CMAKE_OPTIONS)

cmake_build: cmake_config
	cmake --build $(BUILD_DIR)

cmake_test: cmake_build
	cmake --build $(BUILD_DIR) --target test

cmake_coverage: cmake_test
	gcovr -e _build -e tests --sonarqube _build/coverage.xml -r .

cmake_install: cmake_test
	cmake --build $(BUILD_DIR) --target install

clean:
	rm -rf $(BUILD_DIR) $(INSTL_DIR)

clean_all:
	rm -rf _build _install
