// OCR local con el framework Vision de macOS. Uso: ocr_vision imagen.png
// Lo compila bin/adjuntos.py con swiftc la primera vez y lo deja en .cerebro/ocr_vision.
import Foundation
import Vision
import AppKit

let args = CommandLine.arguments
guard args.count > 1, let image = NSImage(contentsOfFile: args[1]),
      let cg = image.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
    FileHandle.standardError.write("no se pudo abrir la imagen\n".data(using: .utf8)!)
    exit(1)
}
let request = VNRecognizeTextRequest()
request.recognitionLevel = .accurate
request.usesLanguageCorrection = true
request.recognitionLanguages = ["en-US", "es-ES"]
let handler = VNImageRequestHandler(cgImage: cg, options: [:])
do {
    try handler.perform([request])
    let lines = (request.results ?? []).compactMap { $0.topCandidates(1).first?.string }
    print(lines.joined(separator: "\n"))
} catch {
    FileHandle.standardError.write("fallo de Vision: \(error)\n".data(using: .utf8)!)
    exit(2)
}
