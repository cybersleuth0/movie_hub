import 'package:flutter/material.dart';
import 'package:movieshub/domain/movie_db.dart';
import 'package:movieshub/ui_pages/movieDetails_page.dart';

class ListofMovies extends StatelessWidget {
  //category index
  final int index;

  ListofMovies({required this.index});

  @override
  Widget build(BuildContext context) {
    print("${movie_db.moviedatabase[index]['movies']}");
    //get all movies in selected category
    final tapcategory = movie_db.moviedatabase[index]["movies"];
    return Scaffold(
        backgroundColor: Colors.black,
        appBar: AppBar(
            centerTitle: true,
            backgroundColor: Colors.black,
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
                      color: const Color(0xfff3bc32)),
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
            )),
        body: GridView.builder(
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                mainAxisSpacing: 11,
                crossAxisSpacing: 11,
                childAspectRatio: 9 / 16),
            itemCount: tapcategory.length,
            itemBuilder: (context, childindex) {
              final movie = tapcategory["movies"];
              return Padding(
                padding: const EdgeInsets.all(2.0),
                child: InkWell(
                  onTap: () {
                    Navigator.push(context,
                        MaterialPageRoute(builder: (context) => DetailsPage()));
                  },
                  child: Stack(children: [
                    //Movie Poster
                    Image.network(movie["movie_Poster"]),
                    //movie name
                    Positioned(
                      bottom: 5,
                      width: 200,
                      child: Container(
                        color: Colors.black54,
                        child: Text(
                          movie["movieName"],
                          overflow: TextOverflow.ellipsis,
                          maxLines: 5,
                          style: const TextStyle(
                              //color: Color(0xfff3bc32),
                              color: Colors.white,
                              fontWeight: FontWeight.bold,
                              fontSize: 15,
                              fontFamily: "Poppins"),
                        ),
                      ),
                    )
                  ]),
                ),
              );
            }));
  }
}
