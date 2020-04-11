# Algorithms on Graphs

## Overview

If you have ever used a navigation service to find optimal route and estimate time to destination, you've used algorithms on graphs. Graphs arise in various real-world situations as there are road networks, computer networks and, most recently, social networks! If you're looking for the fastest time to get to work, cheapest way to connect set of computers into a network or efficient algorithm to automatically find communities and opinion leaders in Facebook, you're going to work with graphs and algorithms on graphs.

In this course, you will first learn what a graph is and what are some of the most important properties. Then you'll learn several ways to traverse graphs and how you can do useful things while traversing the graph in some order. We will then talk about shortest paths algorithms — from the basic ones to those which open door for 1000000 times faster algorithms used in Google Maps and other navigational services. You will use these algorithms if you choose to work on our Fast Shortest Routes industrial capstone project. We will finish with minimum spanning trees which are used to plan road, telephone and computer networks and also find applications in clustering and approximate algorithms.

## Key Concepts by Week

Week 1, Decomposition of Graphs 1
> Graphs arise in various real-world situations as there are road networks, computer networks and, most recently, social networks! If you're looking for the fastest time to get to work, cheapest way to connect set of computers into a network or efficient algorithm to automatically find communities and opinion leaders hot in Facebook, you're going to work with graphs and algorithms on graphs. In this module, you will learn ways to represent a graph as well as basic algorithms for decomposing graphs into parts. In the programming assignment of this module, you will apply the algorithms that you’ve learned to implement efficient programs for exploring mazes, analyzing Computer Science curriculum, and analyzing road networks. In the first week of the module, we focus on undirected graphs.

- Explain what a graph is
- Create a program for exploring mazes

Week 2, Decomposition of Graphs 2
> This week we continue to study graph decomposition algorithms, but now for directed graphs.

- Explain what a directed graph is
- Explain what a topological order is
- Create a program for analyzing a CS curriculum

Week 3, Paths in Graphs 1
> In this module you will study algorithms for finding Shortest Paths in Graphs. These algorithms have lots of applications. When you launch a navigation app on your smartphone like Google Maps or Yandex.Navi, it uses these algorithms to find you the fastest route from work to home, from home to school, etc. When you search for airplane tickets, these algorithms are used to find a route with the minimum number of plane changes. Unexpectedly, these algorithms can also be used to determine the optimal way to do currency exchange, sometimes allowing to earh huge profit! We will cover all these applications, and you will learn Breadth-First Search, Dijkstra's Algorithm and Bellman-Ford Algorithm. These algorithms are efficient and lay the foundation for even more efficient algorithms which you will learn and implement in the Shortest Paths Capstone Project to find best routes on real maps of cities and countries, find distances between people in Social Networks. In the end you will be able to find Shortest Paths efficiently in any Graph. This week we will study Breadth-First Search algorithm.

- Explain what a shortest path is
- Describe algorithms for computing shortest paths in undirected graphs
- Create a program for finding an optimal flight

Week 4, Paths in Graphs 2
> This week we continue to study Shortest Paths in Graphs. You will learn Dijkstra's Algorithm which can be applied to find the shortest route home from work. You will also learn Bellman-Ford's algorithm which can unexpectedly be applied to choose the optimal way of exchanging currencies. By the end you will be able to find shortest paths efficiently in any Graph.

- Explain algorithms for finding shortest paths in weighted graphs
- Create a program for finding a cheapest flight
- Create a program for detecting anomalies in currency exchange rates

Week 5, Minimum Spanning Trees
> In this module, we study the minimum spanning tree problem. We will cover two elegant greedy algorithms for this problem: the first one is due to Kruskal and uses the disjoint sets data structure, the second one is due to Prim and uses the priority queue data structure. In the programming assignment for this module you will be computing an optimal way of building roads between cities and an optimal way of partitioning a given set of objects into clusters (a fundamental problem in data mining).

- Explain what a spanning tree is
- Describe algorithms for computing minimum spanning trees
- Create an efficient program for clustering

Week 6, Advanced Shortest Paths Project (Optional)
> In this module, you will learn Advanced Shortest Paths algorithms that work in practice 1000s (up to 25000) of times faster than the classical Dijkstra's algorithm on real-world road networks and social networks graphs. You will work on a Programming Project based on these algorithms. You will find the shortest paths on the real maps of parts of US and the shortest paths connecting people in the social networks. We encourage you not only to use the ideas from this module's lectures in your implementations, but also to come up with your own ideas for speeding up the algorithm! We encourage you to compete on the forums to see whose implementation is the fastest one :)

- Develop an algorithm to find distances in the graphs of social networks such as Facebook and internet graphs much faster than with the classical approaches
- Develop an algorithm to find distances in the real road networks faster
- Develop Bidirectional Dijkstra, A* (A-star) and Contraction Hierarchies algorithms
- Develop a solution of the central problem of delivery companies - delivery truck route optimization on real-world road network
- Develop an algorithm to find distances in the real-world road networks thousands of times faster than with the classical approaches