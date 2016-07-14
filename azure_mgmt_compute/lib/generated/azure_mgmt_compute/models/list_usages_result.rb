# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Compute
  module Models
    #
    # The List Usages operation response.
    #
    class ListUsagesResult

      include MsRestAzure

      # @return [Array<Usage>] the list Compute Resource Usages.
      attr_accessor :value

      # @return [String] the uri to fetch the next page of Compute Resource
      # Usages. Call ListNext() with this to fetch the next page of Compute
      # Resource Usages.
      attr_accessor :next_link


      #
      # Mapper for ListUsagesResult class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'ListUsagesResult',
          type: {
            name: 'Composite',
            class_name: 'ListUsagesResult',
            model_properties: {
              value: {
                required: false,
                serialized_name: 'value',
                type: {
                  name: 'Sequence',
                  element: {
                      required: false,
                      serialized_name: 'UsageElementType',
                      type: {
                        name: 'Composite',
                        class_name: 'Usage'
                      }
                  }
                }
              },
              next_link: {
                required: false,
                serialized_name: 'nextLink',
                type: {
                  name: 'String'
                }
              }
            }
          }
        }
      end
    end
  end
end