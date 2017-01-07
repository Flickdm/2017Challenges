#include <iostream>
#include <map>

//prototypes
bool getMajorityElement(int *list, int listSize, int &outElement, int &outCount);
void handleInput(int *&list, int &listSize, int &expCount, int &expElement);

int main(int argc, char* argv[]) {

    int numberOfTests = 0;
    std::cin >> numberOfTests;
    std::cin.ignore();

    for(int i = 0; i < numberOfTests; i++) {

        int *inputList;
        int inputListSize = 0;
        int expCount, expElement;
        handleInput(inputList, inputListSize, expCount, expElement);

        int maxCount = 0;
        int maxElement = 0;
        if(!getMajorityElement(inputList, inputListSize, maxCount, maxElement)) {
            std::cout << "[FAIL] Test: " << i << '\n';
        }

        if(maxCount == expCount && maxElement == expElement) {
            std::cout << "[PASS] Test: " << i << '\n';
        } else {
            std::cout << "[FAIL] Test: " << i << '\n';
            std::cout << maxCount << " " << maxElement << std::endl;
            std::cout << expCount << " " << expElement << std::endl;
        }

        delete[] inputList;
    }

}


void handleInput(int *&list, int &listSize, int &expCount, int &expElement) {

    std::cin >> listSize;

    //allocating memory
    list = new int[listSize];

    for(int i = 0; i < listSize; i++) {
        std::cin >> list[i];
    }

    std::cin >> expCount;
    std::cin >> expElement;
}


bool getMajorityElement(int *list, int listSize, int &outCount, int &outElement) {

    if (list == 0) {
        std::cerr << "[ERROR]: Pointer was NULL" << "\n";
        return false;
    }

    int maxCount = -1;
    int maxElement = -1;

    std::map<int, int> counts;

    for (int i = 0; i < listSize; i++) {
        //produces a map of occurences
        counts[list[i]]++;

        if (counts[list[i]] > maxCount) {
            maxCount = counts[list[i]];
            maxElement = list[i];
        }
    }

    if (maxCount <= 0) {
        std::cerr << "[ERROR]: List Size was " << listSize << "\n";
        return false;
    }

    outCount = maxCount;
    outElement = maxElement;

    return true;
}
