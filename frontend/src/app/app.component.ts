// Import the necessary Angular core component module
import { Component } from '@angular/core';
// Import the TranslationService to handle translation logic
import { TranslationService } from './translation.service';

// Define the main component of the application
@Component({
  // Selector to use this component in HTML
  selector: 'app-root',
  // Path to the HTML template for this component
  templateUrl: './app.component.html',
  // Path to the CSS file for styling this component
  styleUrls: ['./app.component.css']
})
// Define the AppComponent class
export class AppComponent {
  // Property to hold the text input from the user
  text: string = '';
  // Property to hold the selected source language, default is German ('de')
  srcLang: string = 'de';
  // Property to hold the selected target language, default is English ('en')
  tgtLang: string = 'en';
  // Property to hold the translated text
  translation: string = '';

  // Constructor to inject the TranslationService
  constructor(private translationService: TranslationService) {}

  // Method to perform the translation
  translate() {
    // Call the translate method from TranslationService, passing the text and language parameters
    this.translationService.translate(this.text, this.srcLang, this.tgtLang).subscribe(
      response => {
        // Log the translation response from the service
        console.log('Translation response:', response);  
        // Update the translation property with the translated text from the response
        this.translation = response.translation;
      },
      // Handle any errors that occur during the translation process
      error => console.error('Error translating text', error)
    );
  }
}
