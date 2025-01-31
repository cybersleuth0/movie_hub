import 'package:flutter/material.dart';
import 'package:movieshub/domain/movie_db.dart';
import 'package:movieshub/ui_pages/movieDetails_page.dart';

class ListofMovies extends StatelessWidget {
  //category index
  final Map<String, dynamic> selectedcategory;
  final genreName;

  ListofMovies({required this.selectedcategory, required this.genreName});

  @override
  Widget build(BuildContext context) {
    //get all movies in selected category
    final tapcategory = selectedcategory;
    final allmovies = tapcategory["movies"];
    return Scaffold(
        backgroundColor: Colors.black,
        appBar: AppBar(
            centerTitle: true,
            backgroundColor: Colors.black,
            title: Text(
              genreName,
              style: const TextStyle(
                  fontFamily: "Merriweather",
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 25),
            )),
        body: GridView.builder(
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                mainAxisSpacing: 11,
                crossAxisSpacing: 11,
                childAspectRatio: 9 / 16),
            itemCount: allmovies.length,
            itemBuilder: (context, index) {
              final movie = allmovies[index];
              return Padding(
                padding: const EdgeInsets.all(2.0),
                child: InkWell(
                  onTap: () {
                    Navigator.push(
                        context,
                        MaterialPageRoute(
                            builder: (context) => DetailsPage(
                                  tapmovie: movie,
                                )));
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
                          movie["movie_Name"],
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
