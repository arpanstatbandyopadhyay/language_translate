// Import the necessary Angular core module for creating services
import { Injectable } from '@angular/core';
// Import HttpClient for making HTTP requests
import { HttpClient } from '@angular/common/http';
// Import Observable from RxJS to handle asynchronous operations
import { Observable } from 'rxjs';

// Mark the class as an injectable service
@Injectable({
  // Provided in the root injector so it's a singleton across the application
  providedIn: 'root'
})
// Define the TranslationService class
export class TranslationService {
  // Define the API URL for the translation service
  private apiUrl = 'http://127.0.0.1:8000/translate/';

  // Constructor to inject the HttpClient
  constructor(private http: HttpClient) {}

  // Method to perform translation by sending a POST request to the API
  translate(text: string, srcLang: string, tgtLang: string): Observable<any> {
    // Create the payload object with the text and language parameters
    const payload = { text, src_lang: srcLang, tgt_lang: tgtLang };
    // Send a POST request to the translation API with the payload and return the observable
    return this.http.post(this.apiUrl, payload);
  }
}
