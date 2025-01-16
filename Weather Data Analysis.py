class Solution:
	def WeatherDataAnalysis(matrix,n,d):
		result = []

		for i in range(d):
			min = float('inf')
			max = float('-inf')
			for j in range(n):
				if matrix[j][i] < min:
					min = matrix[j][i]

				if matrix[j][i] > max:
					max = matrix[j][i]

			result.append((min,max))

		return result


