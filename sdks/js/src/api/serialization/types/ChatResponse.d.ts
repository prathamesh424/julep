/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "..";
import * as JulepApi from "../../api";
import * as core from "../../core";
export declare const ChatResponse: core.serialization.ObjectSchema<
  serializers.ChatResponse.Raw,
  JulepApi.ChatResponse
>;
export declare namespace ChatResponse {
  interface Raw {
    id: string;
    finish_reason: serializers.ChatResponseFinishReason.Raw;
    response: serializers.ChatMlMessage.Raw[][];
    usage: serializers.CompletionUsage.Raw;
    jobs?: string[] | null;
  }
}
