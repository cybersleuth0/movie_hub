import 'dart:ui';
import 'package:flutter/material.dart';

class DetailsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xff121012),
      appBar: AppBar(
          backgroundColor: Colors.black,
          centerTitle: true,
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
      body: SingleChildScrollView(
        child: Column(
          children: [
            // Poster with Gradient
            Stack(
              children: [
                // Main Poster Image with Clipping
                Container(
                  height: 600,
                  decoration: const BoxDecoration(
                    image: DecorationImage(
                      image: NetworkImage(
                        "https://catimages.org/images/2025/01/10/Fateh-2025-HDHub4u.Tv.jpg",
                      ),
                      fit: BoxFit.cover,
                    ),
                  ),
                ),
                //top gradent
                Positioned(
                  top: 0,
                  left: 0,
                  right: 0,
                  child: Container(
                    height: 15,
                    decoration: BoxDecoration(
                      gradient: LinearGradient(
                        begin: Alignment.topCenter,
                        end: Alignment.bottomCenter,
                        colors: [
                          Colors.black.withOpacity(0.5),
                          Colors.transparent,
                        ],
                      ),
                    ),
                  ),
                ),
                // Bottom Gradient
                Positioned(
                  bottom: -20,
                  left: 0,
                  right: 0,
                  child: Container(
                    //height: 300,
                    decoration: BoxDecoration(
                      gradient: LinearGradient(
                        begin: Alignment.topCenter,
                        end: Alignment.bottomCenter,
                        colors: [
                          Colors.transparent,
                          Colors.black.withOpacity(1),
                        ],
                      ),
                    ),
                    child: const Padding(
                      padding: EdgeInsets.all(16.0),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          // Movie Title
                          Text(
                            "Fateh (Full Movie)",
                            textAlign: TextAlign.center,
                            style: TextStyle(
                                color: Colors.white,
                                fontFamily: "OpenSans",
                                fontSize: 28,
                                fontWeight: FontWeight.bold,
                                height: 1.7),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ],
            ),
            //movie details cast director etc
            const Padding(
              padding: EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Text(
                    """
iMDB Rating: x/10
Genre: Action | Crime | Thriller
Stars: Sonu Sood, Jacqueline Fernandez, Vijay Raaz
Director: Sonu Sood
Language: Hindi ORG-DD2.0 / HC-ESub
Quality: PRE-HD 1080p | 720p | 480p
                    """,
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: Colors.white70,
                      fontFamily: "OpenSans",
                      fontSize: 16,
                      height: 1.5,
                    ),
                  ),
                ],
              ),
            ),
            // Movie Name and Details
            Divider(
              color: Colors.grey.withOpacity(0.7),
              height: 0,
              thickness: 2,
            ),
            // Screen Shots Text
            const Padding(
              padding: EdgeInsets.all(16.0),
              child: Text(
                ": Screen-Shots :",
                textAlign: TextAlign.center,
                style: TextStyle(
                  color: Colors.red,
                  fontFamily: "OpenSans",
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            // Screen Shots images
            SizedBox(
                height: 200,
                child: ListView.builder(
                  itemCount: 3,
                  scrollDirection: Axis.horizontal,
                  itemBuilder: (context, index) {
                    return Container(
                      margin: const EdgeInsets.all(8.0),
                      width: 150,
                      decoration: BoxDecoration(
                          color: Colors.grey.shade300,
                          image: const DecorationImage(
                              image: NetworkImage(
                                  "https://catimages.org/images/2025/01/09/vlcsnap-2025-01-09-20h21m18s734.jpg"),
                              fit: BoxFit.cover)),
                    );
                  },
                )),
            const SizedBox(height: 20),
            const Text(
              "Download Fateh (2025) Full Movie in Hindi | HD",
              textAlign: TextAlign.center,
              style: TextStyle(
                  color: Colors.white,
                  fontFamily: "OpenSans",
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                  height: 1.7),
            ),
            const SizedBox(height: 20),
            const Text(": DOWNLOAD LINKS :",
                textAlign: TextAlign.center,
                style: TextStyle(
                  color: Colors.red,
                  fontFamily: "OpenSans",
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                )),
            const SizedBox(height: 5),
            SizedBox(
              height: 200,
              child: ListView.builder(
                itemCount: 1,
                itemBuilder: (context, index) {
                  return Center(
                    child: Padding(
                      padding: const EdgeInsets.only(top: 5),
                      child: Column(
                        children: [
                          const Text(
                            "480p⚡[450MB]",
                            style: TextStyle(
                                color: Colors.blue,
                                fontSize: 20,
                                fontWeight: FontWeight.bold,
                                letterSpacing: 2),
                          ),
                          const SizedBox(height: 10),
                          Divider(
                            color: Colors.grey.withOpacity(0.7),
                            height: 0,
                            thickness: 2,
                          ),
                          const SizedBox(height: 10),
                          const Text(
                            "720p HEVC [760MB]",
                            style: TextStyle(
                                color: Colors.blue,
                                fontSize: 20,
                                fontWeight: FontWeight.bold,
                                letterSpacing: 2),
                          ),
                        ],
                      ),
                    ),
                  );
                },
              ),
            )
          ],
        ),
      ),
    );
  }
}
