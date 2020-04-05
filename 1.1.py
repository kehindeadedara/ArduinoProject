## Given the array of integer, return a new array such that it wil return the product of array at index, excluding i.
## for example inout is [1,2,3,4,5,6] output will be [120,60,40,30,24]


nums = [1,2,3,4,5]
#generate prefix product
def products(nums):
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1]*num)
        else:
            prefix_products.append(num)


    suffix_product = []

    for num in reversed(nums):
        if suffix_product:
            suffix_product.append(suffix_product[-1]*num)
        else:
            suffix_product.append(num)
    # suffix_product = list(reversed(suffix_product))

    result = []
    for i in range(len(nums)):
        if i ==0:
            result.append(suffix_product[i+1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i-1])
        else:
            result.append(
                prefix_products[i-1] * suffix_product[i+1]
            )

    return result, prefix_products,suffix_product

print(products(nums))
