import 'package:flutter/material.dart';
import 'package:movieshub/domain/movie_db.dart';
import 'package:movieshub/ui_pages/showmovies_Page.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xff121012),
      appBar: AppBar(
        centerTitle: true,
        backgroundColor: const Color(0xff121012),
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text(
              "Movies ",
              style: TextStyle(
                  fontFamily: "Merriweather",
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 25),
            ),
            Container(
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(5),
                color: const Color(0xfff3bc32),
              ),
              padding: const EdgeInsets.symmetric(horizontal: 5),
              child: const Text(
                "Hub",
                style: TextStyle(
                    fontFamily: "Merriweather",
                    fontSize: 25,
                    fontWeight: FontWeight.bold,
                    color: Colors.black),
              ),
            ),
          ],
        ),
      ),
      body: ListView(
        children: [
          // Text: What would you like to watch?
          const Center(
            child: Padding(
              padding: EdgeInsets.all(20.0),
              child: Text(
                "What would you\n\t\tlike to watch?",
                style: TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                    fontSize: 29.36,
                    fontFamily: "OpenSans"),
              ),
            ),
          ),
          // Search bar
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 10),
            child: Container(
              decoration: BoxDecoration(
                  color: const Color(0xff382C3E),
                  borderRadius: BorderRadius.circular(20)),
              padding: const EdgeInsets.all(5),
              child: const Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Icon(
                    Icons.search,
                    size: 30,
                    color: Colors.white30,
                  ),
                  SizedBox(width: 10),
                  Expanded(
                    child: TextField(
                      decoration: InputDecoration(
                        hintText: "Search",
                        hintStyle: TextStyle(color: Colors.white30),
                        border: InputBorder.none,
                      ),
                      style: TextStyle(color: Colors.white),
                    ),
                  ),
                  Icon(
                    Icons.mic,
                    size: 30,
                    color: Colors.white30,
                  ),
                ],
              ),
            ),
          ),
          sizespace(),
          ListView.builder(
              physics: NeverScrollableScrollPhysics(),
              shrinkWrap: true,
              itemCount: movie_db.moviedatabase.length,
              itemBuilder: (context, index) {
                return Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    sizespace(),
                    movieCategoryname(
                        category_Name: movie_db.moviedatabase[index]["GENREs"]),
                    sizespace(), //sizebox 20 height
                    // Latest Releases (Horizontal ListView)
                    horizontalScroll(index),
                  ],
                );
              })
        ],
      ),
    );
  }

  Widget sizespace({double high = 20}) {
    return SizedBox(height: high);
  }

  Widget movieCategoryname({required String category_Name}) {
    return Padding(
      padding: const EdgeInsets.only(left: 20),
      child: Text(
        "${category_Name}",
        style: const TextStyle(
            color: Colors.white70,
            fontFamily: "OpenSans",
            fontWeight: FontWeight.bold,
            fontSize: 17.83),
      ),
    );
  }

  Widget horizontalScroll(int index) {
    return SizedBox(
      height: 200,
      child: ListView.builder(
        itemCount: movie_db.moviedatabase[index]["movies"].length,
        scrollDirection: Axis.horizontal,
        itemBuilder: (context, childIndex) {
          final selectedcategory = movie_db.moviedatabase[index];
          return Padding(
            padding: const EdgeInsets.only(left: 20),
            child: InkWell(
              onTap: () {
                Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (context) => ListofMovies(
                            selectedcategory: selectedcategory,
                            genreName: selectedcategory["GENREs"])));
              },
              child: Container(
                width: 150,
                decoration: BoxDecoration(
                    color: Colors.grey.shade300,
                    borderRadius: BorderRadius.circular(20),
                    image: DecorationImage(
                        image: NetworkImage(movie_db.moviedatabase[index]
                            ["movies"][childIndex]['movie_Poster']),
                        fit: BoxFit.cover)),
              ),
            ),
          );
        },
      ),
    );
  }
}
