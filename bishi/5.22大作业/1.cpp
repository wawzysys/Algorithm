#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Process
{
public:
    int id;
    int arrivalTime;
    int burstTime;
    int startTime;
    int completionTime;
    int turnaroundTime;
    int waitingTime;

    Process(int id, int arrivalTime, int burstTime)
    {
        this->id = id;
        this->arrivalTime = arrivalTime;
        this->burstTime = burstTime;
    }
};

bool compareArrival(Process &p1, Process &p2)
{
    return p1.arrivalTime < p2.arrivalTime;
}

void fcfs(vector<Process> &processes)
{
    sort(processes.begin(), processes.end(), compareArrival);

    int currentTime = 0;
    for (auto &process : processes)
    {
        if (currentTime < process.arrivalTime)
        {
            currentTime = process.arrivalTime;
        }
        process.startTime = currentTime;
        process.completionTime = process.startTime + process.burstTime;
        process.turnaroundTime = process.completionTime - process.arrivalTime;
        process.waitingTime = process.turnaroundTime - process.burstTime;

        currentTime = process.completionTime;
    }
}

int main()
{
    vector<Process> processes = {
        Process(1, 0, 4),
        Process(2, 1, 3),
        Process(3, 2, 1)};

    fcfs(processes);

    cout << "ID\tAT\tBT\tST\tCT\tTAT\tWT\n";
    for (const auto &process : processes)
    {
        cout << process.id << "\t"
             << process.arrivalTime << "\t"
             << process.burstTime << "\t"
             << process.startTime << "\t"
             << process.completionTime << "\t"
             << process.turnaroundTime << "\t"
             << process.waitingTime << "\n";
    }

    return 0;
}
