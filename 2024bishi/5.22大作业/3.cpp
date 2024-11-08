#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct IORequest
{
    int deviceId;
    int requestTime;
    int duration;
    IORequest(int id, int time, int dur) : deviceId(id), requestTime(time), duration(dur) {}
};

class DeviceScheduler
{
private:
    queue<IORequest> requests;
    int currentTime;
    vector<int> responseTimes;

public:
    DeviceScheduler() : currentTime(0) {}

    void addRequest(IORequest req)
    {
        requests.push(req);
    }

    void processRequests()
    {
        while (!requests.empty())
        {
            IORequest current = requests.front();
            requests.pop();
            // 模拟时间流逝至请求开始
            currentTime = max(currentTime, current.requestTime);
            int startTime = currentTime;
            currentTime += current.duration;
            int responseTime = currentTime - current.requestTime;
            responseTimes.push_back(responseTime);

            cout << "Processing request from Device " << current.deviceId
                 << " | Start time: " << startTime
                 << " | Duration: " << current.duration
                 << " | End time: " << currentTime
                 << " | Response Time: " << responseTime << endl;
        }
    }

    void evaluatePerformance()
    {
        if (responseTimes.empty())
            return;
        int totalResponseTime = 0;
        for (int time : responseTimes)
        {
            totalResponseTime += time;
        }
        double averageResponseTime = double(totalResponseTime) / responseTimes.size();
        cout << "Average Response Time: " << averageResponseTime << " units" << endl;
    }
};

int main()
{
    DeviceScheduler scheduler;
    scheduler.addRequest(IORequest(1, 1, 3));
    scheduler.addRequest(IORequest(2, 2, 2));
    scheduler.addRequest(IORequest(3, 3, 1));

    scheduler.processRequests();
    scheduler.evaluatePerformance();

    return 0;
}
