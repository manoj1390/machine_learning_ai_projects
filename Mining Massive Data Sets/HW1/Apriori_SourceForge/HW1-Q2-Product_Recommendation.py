# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:19:00 2016

@author: mravi
"""
import itertools

#to pickup all possible combinations of baskets
def basket_finder(f):
    with open(f,'r') as f:
        for line in f:
            b=line.split(' ')
            yield b
            
            
            
            
#to count all possible combinations of itemset sizes
def counter(i,ref_dict):
    if i in ref_dict:
        ref_dict[i]+=1
    else:
        ref_dict[i]=1
    return ref_dict
    
    
    
    
    
def main():
    f = '/Users/mravi/Desktop/C/MMDS - Sta/HW/HW1/browsing.txt'
    s=100
    
    
    
    single_dict={}
    frequent_singles={}
    #Getting frequent single itemsets
    for b in basket_finder(f):
        for i in b:
            single_dict =counter(i,single_dict)
    for key in single_dict:
        if key !='\n':
            if single_dict[key]>=s:
                frequent_singles[key]=single_dict[key]
    
    
    
    
    
    double_dict={}
    frequent_pairs={}
    #Getting the frequent paired itemsets
    for b in basket_finder(f):
        #generating all possible pairs for a given basket
        #Filtering based on frequently occuring single itemsets
        frequent_singles_list = [x for x in b if x in frequent_singles]
        frequent_singles_list.sort()
        #b.sort()
        possible_pairs = itertools.combinations(frequent_singles_list, 2)
        for p in possible_pairs:
            double_dict=counter(p,double_dict)
    for key in double_dict:
        if key !='\n':
            if double_dict[key]>=s:
                frequent_pairs[key]=double_dict[key]
                
                
                
                
                
    triple_dict={}
    frequent_triples={}
    #Getting the frequent triple itemsets
    for b in basket_finder(f):
        addnl = []
        b.sort()
        
        possible_pairs = itertools.combinations(b, 2)
        for p in possible_pairs:
        #picking up triplet sets
            if p in frequent_pairs:
                for s in p:
                    if s!='\n':
                        if s not in addnl:
                            addnl.append(s)
        addnl.sort()
        possible_triples = itertools.combinations(addnl, 3)
        for q in possible_triples:
            triple_dict=counter(q,triple_dict)
        
    for key in triple_dict:
        if key !='\n':
            if triple_dict[key]>=s:
                frequent_triples[key]=triple_dict[key]
                

    #Calculating confidence scores
    
    #for pairs
    
    c_p_list = []
    for i in frequent_pairs:
        x=itertools.combinations(i,1)
        for obj in x:
            if len(obj)==1:
                obj=obj[0]
            #if key in frequent_pairs!='\n' & key in frequent_singles!='\n':
                conf = float(frequent_pairs[i])/float(frequent_singles[obj])
                c_p_list.append(conf)
    
    c_p_list.sort()
    
    #for triples
    
    c_t_list = []
    
    for j in frequent_triples:
        x=itertools.combinations(i,2)
        for obj in x:
            if len(obj)==1:
                obj=obj[0]
            #if key in frequent_pairs!='\n' & key in frequent_triples!='\n':
                conf = float(frequent_triples[j])/float(frequent_pairs[obj])
                c_t_list.append(conf)
    
    c_t_list.sort()
        
if __name__ == '__main__':
    main()