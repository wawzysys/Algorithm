#include <iostream>
#include <list>
#include <unordered_map>
#include <vector>

using namespace std;

class MemoryManager
{
private:
    int partitionSize;
    int numPartitions;
    vector<bool> partitions;
    list<int> lruQueue;  // For LRU algorithm
    list<int> fifoQueue; // For FIFO algorithm
    unordered_map<int, int> pageTable;

public:
    MemoryManager(int totalSize, int partitionSize) : partitionSize(partitionSize)
    {
        numPartitions = totalSize / partitionSize;
        partitions.assign(numPartitions, false);
    }

    int allocate()
    {
        for (int i = 0; i < numPartitions; i++)
        {
            if (!partitions[i])
            {
                partitions[i] = true;
                return i;
            }
        }
        return -1; // No free partition
    }

    void free(int partitionIndex)
    {
        if (partitionIndex >= 0 && partitionIndex < numPartitions)
        {
            partitions[partitionIndex] = false;
        }
    }

    void accessPage(int pageNumber)
    {
        if (pageTable.find(pageNumber) == pageTable.end())
        { // Page fault
            int freePartition = allocate();
            if (freePartition == -1)
            {
                freePartition = replacePageFIFO();
            }
            pageTable[pageNumber] = freePartition;
            fifoQueue.push_back(pageNumber);
            lruQueue.remove(pageNumber);
            lruQueue.push_back(pageNumber);
        }
        else
        {
            lruQueue.remove(pageNumber);
            lruQueue.push_back(pageNumber);
        }
    }

    int replacePageFIFO()
    {
        int oldPage = fifoQueue.front();
        fifoQueue.pop_front();
        int partitionIndex = pageTable[oldPage];
        pageTable.erase(oldPage);
        return partitionIndex;
    }

    double calculateMemoryUtilization()
    {
        int usedPartitions = 0;
        for (bool status : partitions)
        {
            if (status)
                usedPartitions++;
        }
        return (double)usedPartitions / numPartitions * 100.0;
    }

    void displayMemoryStatus()
    {
        cout << "Memory Utilization: " << calculateMemoryUtilization() << "%" << endl;
        cout << "Partitions: ";
        for (int i = 0; i < numPartitions; i++)
        {
            cout << (partitions[i] ? "Used" : "Free") << " ";
        }
        cout << endl;
    }
};

int main()
{
    MemoryManager mm(100, 10);
    mm.accessPage(1);
    mm.accessPage(2);
    mm.accessPage(3);
    mm.displayMemoryStatus();
    mm.accessPage(1);
    mm.displayMemoryStatus();

    return 0;
}
