import 'dart:async';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:movieshub/ui_pages/homepage.dart';

class SplashScreen extends StatefulWidget {
  @override
  State<SplashScreen> createState() => SplashScreenState();
}

class SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    Timer(Duration(seconds: 2), () {
      Navigator.pushReplacement(
          context, MaterialPageRoute(builder: (context) => HomePage()));
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
            gradient: LinearGradient(colors: [
          Color(0xff141E30),
          Color(0xff243B55),
        ])),
        alignment: Alignment.center,
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text(
              "Movies ",
              style: TextStyle(
                  fontFamily: "Merriweather",
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 52),
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
                    fontSize: 52,
                    fontWeight: FontWeight.bold,
                    color: Colors.black),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
