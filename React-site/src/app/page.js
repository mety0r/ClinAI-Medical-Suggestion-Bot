

import Image from "next/image";
import Link from "next/link";

export default function Home() {
    return (
        <>
            <div className="flex flex-row bg-black justify-between">
                <div className="justify-start p-5">
                    <h1 className="text-4xl text-yellow-400 font-bold ">Clin AI</h1>
                </div>

                <div className="p-5 gap-5 justify-end">
                    <Link href="http://localhost:8001" className="bg-black text-xl hover:text-yellow-400 mr-10 text-white font-bold py-4 px-6 rounded">
                        MedBot
                    </Link>
                    <Link href="http://localhost:8002" className="bg-black text-xl hover:text-yellow-400 text-white font-bold py-4 px-6 rounded">
                        Report Analyzer
                    </Link>
                </div>
            </div>
            <main className="flex flex-row min-h-screen bg-black text-white items-center p-24">
                <div className="lg:w-1/2 items-center flex flex-col break-words justify-center">
                    <div className="mb-10">
                        <h1 className="text-3xl font-bold animate-bounce text-yellow-400 mb-5 ">
                            Clin AI - Your Intelligent Healthcare Assistant
                        </h1>
                        <p className=" text-sm font-mono text-gray-200">
                            Welcome to Clin AI, your trusted partner in managing health and wellness.
                            Clin AI leverages advanced artificial intelligence to provide instant medical suggestions through a simple and intuitive chat interface.
                            Whether you have a quick question about symptoms, need advice on managing chronic conditions, or are seeking information on medications, Clin AI is here to help 24/7.
                            Our AI-driven chatbot is designed to offer reliable and accurate health guidance, ensuring you have the information you need to make informed decisions about your health.
                        </p>
                    </div>
                    <div className="gap-5">
                        <h1 className="text-3xl font-bold animate-bounce mb-5 text-yellow-400">
                            Medical Insight Analyzer
                        </h1>
                        <p className="text-sm font-mono text-gray-200">
                            Introducing our state-of-the-art Medical Insight Analyzer, a powerful tool designed to transform how you interact with medical literature.
                            Utilizing Retrieval-Augmented Generation (RAG) technology, our application can analyze vast collections of medical documents to provide comprehensive insights and summaries.
                            Whether you're a healthcare professional looking for the latest research or a patient seeking detailed information on a medical condition, our Medical Insight Analyzer delivers precise and relevant information, helping you stay informed and empowered in your healthcare journey.
                        </p>

                    </div>
                </div>
                <div className="w-1/2 ml-24 flex flex-col items-center justify-center">
                    <div>
                        <img src="./logo.jpg" className=" h-96" />
                    </div>
                </div>

                <h1 className="text-white mt-[600px] w-36"></h1>

            </main>

        </>
    );
}

