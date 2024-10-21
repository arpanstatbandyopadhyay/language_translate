import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TranslationService {
  private apiUrl = 'http://127.0.0.1:8000/translate/';

  constructor(private http: HttpClient) {}

  translate(text: string, srcLang: string, tgtLang: string): Observable<any> {
    const payload = { text, src_lang: srcLang, tgt_lang: tgtLang };
    return this.http.post(this.apiUrl, payload);
  }
}
