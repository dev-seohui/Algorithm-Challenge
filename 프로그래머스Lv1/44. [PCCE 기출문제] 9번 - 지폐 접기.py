def solution(wallet, bill):
    answer = 0
    
    max_wallet, min_wallet  = max(wallet), min(wallet)
    max_bill, min_bill = max(bill), min(bill)
    # print(max_bill, min_bill)
    while True:
        if max_wallet >= max_bill and min_wallet >= min_bill:
            return answer
        else:
            max_bill, min_bill = max(max_bill//2, min_bill), min(max_bill//2, min_bill)
            # print(max_bill, min_bill)
            answer += 1
