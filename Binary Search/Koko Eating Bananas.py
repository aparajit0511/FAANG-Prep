class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = sum(piles)
        copy_piles = piles[:]

        k = 1

        while k <= max_k+1:
            copy_piles = piles[:]
            
            hours = h

            for i in range(len(copy_piles)):
                # print("hi",hours,k,copy_piles,"ivalue: " ,i)
                while hours > 0:
                    if copy_piles[i] > 0:
                            copy_piles[i] -= k
                    else:
                        break

                    hours -= 1

            all_negative = all(num <= 0 for num in copy_piles)

            if all_negative:
                # print(copy_piles,hours,k)
                return k


            k += 1


        return k



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = sum(piles)
        copy_piles = piles[:]

        k = 1

        start , end  = k , max_k+1

        while start <= end:
            mid = (start + end) // 2

            copy_piles = piles[:]
            
            hours = h

            for i in range(len(copy_piles)):
                # print("hi",hours,k,copy_piles,"ivalue: " ,i)
                while hours > 0:
                    if copy_piles[i] > 0:
                            copy_piles[i] -= mid
                    else:
                        break

                    hours -= 1

            all_negative = all(num <= 0 for num in copy_piles)

            if hours == 0 and all_negative:
                return mid
            elif hours > 0 and not all_negative:
                start = mid + 1

            else:
                end = mid - 1

        return k



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start , end = 1 , max(piles)
        result = end

        while start <= end:

            mid = (start + end) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/mid)

            if hours <= h:
                result = min(result,mid)
                end = mid -1
            else:
                start = mid + 1

        return result

