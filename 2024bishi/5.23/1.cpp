#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

// Function to apply the bilateral filter
vector<vector<int>> applyBilateralFilter(const vector<vector<int>> &image, double sigma_d, double sigma_r)
{
    int n = image.size();
    vector<vector<int>> result(n, vector<int>(n, 0));

    // Iterate over each pixel
    for (int x = 0; x < n; x++)
    {
        for (int y = 0; y < n; y++)
        {
            double weight_sum = 0.0;
            double weighted_sum = 0.0;

            // Apply 3x3 filter kernel
            for (int i = -1; i <= 1; i++)
            {
                for (int j = -1; j <= 1; j++)
                {
                    int nx = x + i;
                    int ny = y + j;

                    // Check bounds
                    if (nx >= 0 && nx < n && ny >= 0 && ny < n)
                    {
                        double space_weight = exp(-((i * i + j * j) / (2 * sigma_d * sigma_d)));
                        double range_weight = exp(-((pow(image[x][y] - image[nx][ny], 2)) / (2 * sigma_r * sigma_r)));
                        double weight = space_weight * range_weight;

                        weighted_sum += image[nx][ny] * weight;
                        weight_sum += weight;
                    }
                }
            }

            // Normalize and round the result
            int pixel_value = round(weighted_sum / weight_sum);
            result[x][y] = min(max(pixel_value, 0), 255);
        }
    }
    return result;
}

// Function to read the image
void readImage(vector<vector<int>> &image)
{
    for (auto &row : image)
    {
        for (auto &pixel : row)
        {
            cin >> pixel;
        }
    }
}

// Function to print the filtered image
void printImage(const vector<vector<int>> &image)
{
    for (const auto &row : image)
    {
        for (const auto &pixel : row)
        {
            cout << pixel << endl;
        }
    }
}

int main()
{
    int n;
    cin >> n; // Read the size of the image
    vector<vector<int>> image(n, vector<int>(n));

    readImage(image); // Read the image

    // Filter parameters
    double sigma_d = 1.0;
    double sigma_r = 25.0;

    // Apply the bilateral filter
    vector<vector<int>> filtered_image = applyBilateralFilter(image, sigma_d, sigma_r);

    // Print the filtered image
    printImage(filtered_image);

    return 0;
}
